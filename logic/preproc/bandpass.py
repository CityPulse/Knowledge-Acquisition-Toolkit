__author__ = 'frieder'
import numpy as np
import scipy as s


class bandpass():
    def process(self, window, output_length):
        data = np.array_split(window, output_length)
        result = []

        for section in data:
            fft = s.fft(section)
            bp = fft[:]
            for i in range(len(bp)): # (H-red)
                if i>=2000:bp[i]=0
            ibp=s.ifft(bp)
        result.append(ibp)
        #print fftd.shape
        #result = np.array(result)
        #print "paa output shape", result.shape
        #print "flatted", np.hstack(result)
        #print "flatted", np.hstack(result).shape

        return  (np.hstack(result))

    def getConfigurationParams(self):
        return {"window_length": "100"}