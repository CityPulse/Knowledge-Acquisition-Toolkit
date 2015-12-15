__author__ = 'shirin'
import numpy as np
import math
import bottleneck as bn
class norm():
    def process(self, window):
        data = np.array_split(window, 1)
        result = []
        for section in data:
            result.append( (section-section.min()) / (section.max()-section.min()) )
        result = np.array(result)
        #print "paa output shape", result.shape
        print(result)
        return result

    def getConfigurationParams(self):
        []#return()

