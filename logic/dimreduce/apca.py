from __future__ import division
import math

__author__ = 'eris'
import pywt
import matplotlib.pyplot as plt
import random
import utils

C = [7,5,5,3,3,3,4,6]

def simpleHaarStep(list,coefficients = []):
    if not utils.is_power2(len(list)):
        print "list not power of 2"
        return None
    averages = []
    ctmp = []
    i = 0
    while i < len(list)-1:
        avg = (list[i] + list[i+1])/2
        averages.append(avg)
        ctmp.append(avg-list[i+1])
        i+=2
    coefficients.append(ctmp)
    return averages,coefficients

def simpleHaar(data, coefficients = []):
    if len(data) == 1:
        coefficients.sort(key=len)
        return data, coefficients
    else:
        d,c = simpleHaarStep(data,coefficients)
        return simpleHaar(d,c)

## ACHTUNG ZAEHL FEHLER BEI LEVEL
def normalize(coeffs):
    ret = []
    level = len(coeffs)
    i = 0
    while i <level:
        ll = i
        divisor = math.pow(2,ll/2)
        for k in coeffs[i]:
            ret.append(k/divisor)
        i+=1
    return ret

def magnitude(list,bool=True):
    list.sort(key=abs,reverse=True)
    return list


def reconstruction(avg,coeffs):
    if not coeffs:
        return avg
    jo = []
    i = 0
    for a in avg:
        #print "Debug",a,avg,coeffs,i
        if coeffs != []:
            c = coeffs[i]
            #print "Debug2",a+c,a-c
            jo.append(a+c)
            jo.append(a-c)
            i+=1
    return reconstruction(jo,coeffs[i:])

def unpack(list):
    ret = []
    for i in list:
        for g in i:
            ret.append(g)
    return ret

def dups(list, t):
    if t == 1:
        return list
    ret = []
    for i in list:
        g = 0
        while g<t:
            ret.append(i)
            g+=1
    return ret

def merge(list, M):
    while len(list)>M:
        err,pos = findSmallestError(list)

        list[pos] =err
        list.pop(pos+1)
    return list

def findSmallestError(list):
    i = 0
    err = (list[0]+list[1])/2
    pos = 0
    while i<len(list)-1:
        e =  (list[i]+list[i+1])/2
        if e < err:
            err = e
            pos = i
        i+=1
    return err, pos

def demo1():
    l = 16
    t = 16

    data1 = [math.sin(i) for i in range(0,l)]
    data = data1
    ao,c = simpleHaar(data)
    print ao,c
    jaha = normalize(c)
    co=unpack(c)

    c =  magnitude(jaha,False)
    c.insert(0,ao[0])
    a,c =  utils.zerotrunk(c,t)

    rec =  reconstruction([a],c)


    c =  magnitude(co,False)
    c.insert(0,ao[0])
    a,c =  utils.zerotrunk(c,t)
    rec2 =  reconstruction([a],c)
    print rec

    plt.plot(data)
    plt.plot(dups(rec,l/t))
    plt.plot(dups(rec2,l/t))
    plt.show()
def demo2():
    data = [random.randint(0,10) for i in range(0,8)]
    a1,c1 = simpleHaar(data)

    print "wav1",a1,unpack(c1),c1
    c1 =  unpack(c1)
    rec = reconstruction(a1,c1)
    (a, d) = pywt.dwt(data, "haar" )
    print "wav2",a,d
    recD = pywt.waverec([a,d],"haar")



    print "orig",data
    print "my",rec
    print "yp",recD

    plt.plot(data)
    plt.plot(rec)
    plt.show()


    print a,d
#demo1()
def demo3():
    print C
    a,c = simpleHaar(C)
    print a,c
    #c = normalize(c)

    c = unpack(c)
    print c
    #c = magnitude(c)
    print c
    c.insert(0,a[0])
    print "Original Data",C
    a,c = utils.zerotrunk(c,4)
    print "data to reconstruct from",a,c
    rec =  reconstruction([a],c)
    print "reconstructed",rec
    m=merge(rec,4)
    print "merged",m
    l = dups(m,2)
    print "lengthened",l

    plt.plot(C)
    plt.plot(l)
    plt.show()

def apca(C):
    a,c = simpleHaar(C)
    c = unpack(c)
    c.insert(0,a[0])
    return c
def reconstruct(coeffs, trunkate,originalLength):
    a,c = utils.zerotrunk(coeffs,trunkate)
    rec =  reconstruction([a],c)
    m=merge(rec,trunkate)

    #l = dups(m,2)
    ret = utils.extendV(m,originalLength)
    return ret

