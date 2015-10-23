import math

__author__ = 'eris'
import pywt
import matplotlib.pyplot as plt
import utils
#data = [i for i in range(0,8)]
class dwt():
    def wavelet(self, data):
        (a, d) = pywt.dwt(data, "haar")
        return a, d

    def reconstruct(self, coeff, trunk):
        a, d = coeff
        return pywt.waverec([a[0:trunk], d[0:trunk]], 'haar')

    def process(self, data, output_length):
        return self.reconstruct(self.wavelet(data), output_length)

    def getConfigurationParams(self):
        return {"output_length":"1024"}

