__author__ = 'frieder'
import numpy as np

class minmax():
    def process(self, window, output_length):

        data = np.array_split(window, output_length)
        result = []
        for section in data:

            result.append(section.max()-section.min())
        result = np.array(result)
        return result

    def getConfigurationParams(self):
        return {"window_length":"100"}
