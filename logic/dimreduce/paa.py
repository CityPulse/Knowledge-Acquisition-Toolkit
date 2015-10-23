__author__ = 'eris'
import numpy as np
from scipy.stats import norm
import string
import bottleneck as bn
import math
# paa tranformation, window = incoming data, string_length = length of outcoming data

class paa():
    def process(self, window, output_length):
        data = np.array_split(window, output_length)
        result = []
        for section in data:
            if math.isnan(bn.nanmean(section)):
                result.append(0)
            else:
                result.append(bn.nanmean(section))
        result = np.array(result)
        print "paa output shape", result.shape
        return result

    def getConfigurationParams(self):
        return {"output_length":"100"}