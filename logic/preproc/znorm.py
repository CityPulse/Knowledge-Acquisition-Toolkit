__author__ = 'shirin'
import numpy as np
import math
import bottleneck as bn
class znorm():
    def process(self, window, output_length):
        data = np.array_split(window, 1)
        result = []
        for section in data:
           result.append( (section-section.mean()) / section.std() )
        result = np.array(result)
        #print "paa output shape", result.shape
        return result

    def getConfigurationParams(self):
        return {"Output_length":"1"}

