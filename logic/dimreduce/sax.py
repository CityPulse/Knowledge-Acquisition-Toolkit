from __future__ import division
__author__ = 'Eris, Shirin'
import numpy as np
from scipy.stats import norm
import string
import bottleneck as bn
import math

# paa tranformation, window = incoming data, string_length = length of outcoming data

class sax():
    def process(self, window, output_length, sax_vocab):
        sax = to_sax(to_paa(normalize(window),output_length),sax_vocab)
        #return vocabToCoordinates(len(window),output_length,sax[0],4)
        return vocabToCoordinates(output_length,output_length,sax[0],sax_vocab)

    def getConfigurationParams(self):
        return {"output_length":"100","sax_vocab":"4"}

def normalize(data):
    data2 = np.array(data)
    data2 = data2 - (np.mean(data))
    data2 = data2 /data2.std()
    return data2

def to_paa(data,string_length):
    data = np.array_split(data, string_length)
    return  [np.mean(section) for section in data]


def gen_breakpoints(symbol_count):
    breakpoints = norm.ppf(np.linspace(1. / symbol_count, 1 - 1. / symbol_count, symbol_count - 1))
    breakpoints = np.concatenate((breakpoints, np.array([np.Inf])))
    return breakpoints


def to_sax(data,symbol_count):
    breakpoints = gen_breakpoints(symbol_count)
    locations =  [np.where(breakpoints > section_mean)[0][0] for section_mean in data]
    return [''.join([string.ascii_letters[ind] for ind in locations])]

def vocabToCoordinates(time_window, phrase_length, phrases, symbol_count):
    breakpoints = gen_breakpoints(symbol_count)
    newCutlines = breakpoints.tolist()
    max_value = breakpoints[symbol_count - 2] + ((breakpoints[symbol_count - 2] - breakpoints[symbol_count - 3]) * 2)
    # HERE IS SOMETHING WRONG // ONLY IN VISUALISATION
    min_value = breakpoints[0] - ((breakpoints[1] - breakpoints[0]) * 2)
    infi =  newCutlines.pop()
    newCutlines.append(max_value)
    newCutlines.append(infi)
    newCutlines.insert(0, min_value)
    #newCutlines.insert(0,-np.Inf)
    co1 = time_window / float(phrase_length)

    g = 0
    retList = []
    for s in phrases:
        if s is "#":
            for i in range(int(co1)):
                retList.append(np.NaN)
                g+=1
        else:
            for i in range(int(co1)):
                retList.append(newCutlines[ord(s) - 97])
                g+=1
        #print co1,time_window,phrase_length,g,len(phrases)
    return retList


def convertSaxBackToContinious(string_length, symbol_count, data):
    points, phrases = norm(data,string_length, symbol_count)
    retList = vocabToCoordinates(data, string_length, phrases, points, symbol_count)
    #print phrases[0]
    return retList

def saxDistance(w1, w2,original_length,symbol_count):
    if len(w1) != len(w2):
        raise Exception("not equal string length")
    string_length=len(w1)
    dist = 0
    for (l, k) in zip(w1, w2):
        dist += saxDistanceLetter(l, k,symbol_count)
    result = np.sqrt(dist) * np.sqrt(np.divide(original_length, string_length))
    return result

def saxDistanceLetter(w1, w2, symbol_count):
    n1 = ord(w1) - 97
    n2 = ord(w2) - 97
    lookupTable= createLookup(symbol_count,gen_breakpoints(symbol_count))
    if n1 > symbol_count:
        raise Exception(" letter not in Dictionary " + w1)
    if n2 > symbol_count:
        raise Exception(" letter not in Dictionary " + w2)

    return lookupTable[n1][n2]

def createLookup(symbol_count, breakpoints):
    return make_matrix(symbol_count, symbol_count, breakpoints)


def make_list(row, size, breakpoints):
    mylist = []
    for i in range(size):
        i = i + 1
        if abs(row - i) <= 1:
            mylist.append(0)
        else:
            v = breakpoints[(max(row, i) - 2)] - breakpoints[min(row, i) - 1]
            mylist.append(v)
    return mylist


def make_matrix(rows, cols, breakpoints):
    matrix = []
    for i in range(rows):
        i = i + 1
        matrix.append(make_list(i, cols, breakpoints))
    return matrix