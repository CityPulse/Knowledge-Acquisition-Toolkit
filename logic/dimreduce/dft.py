__author__ = 'eris'
# AGRAWAL, R., FALOUTSOS, C., AND SWAMI, A. 1993. Efficient similarity search in sequence databases.
# In Proceedings of the 4th Conference on Foundations of Data Organization and Algorithms.
#
# The distance function is very Important

#http://www.nbtwiki.net/doku.php?id=tutorial:the_discrete_fourier_transformation_dft#tutorialfourier_transform_and_reconstruction_of_a_simple_signal



import numpy as np
import scipy as s
class dft():


    def process(self, data, output_length):
        fft = np.fft.rfft(data)
        fft = fft[:output_length]
        rfft = np.fft.irfft(fft)
        print rfft.shape
        return rfft

    def getConfigurationParams(self):
        return {"output_length":"100"}
