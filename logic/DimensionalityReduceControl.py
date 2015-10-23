__author__ = 'frieder'
import utils.ClazzLoader
from logic.dimreduce import paa
from logic.dimreduce import dwt
from logic.dimreduce import sax
from logic.dimreduce import dft

class DimensionalityReduceControl(object):
    _instance = None

    def __init__(self, ):
        #TODO: load available algorithms automatically
        self.algorithms = {"paa": "Piecewise Aggregation Approximation", "sax": "Symbolic Aggregate Approximation",
                           "dwt": "Discrete Wavelet Transformation", "dft": "Discrete Fourier Transformation"}
        self.selected = None

        # Has to be initialised due to py2exe
        paa.paa().getConfigurationParams()
        dwt.dwt().getConfigurationParams()
        sax.sax().getConfigurationParams()
        dft.dft().getConfigurationParams()

        self.module_path = "logic.dimreduce."

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DimensionalityReduceControl, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def getAvailableAlgorithms(self):
        return self.algorithms

    def selectAlgorithm(self, index):
        algo = self.algorithms.keys()[index]
        self.selected = utils.ClazzLoader.loadClazz(self.module_path + algo, algo)

    def reduceData(self, data, params):
        _ins = self.selected()
        needed_params = _ins.getConfigurationParams().keys()
        params2 = [params[p] for p in needed_params]
        return _ins.process(data, *params2)

    def getRequiredParameters(self):
        return self.selected().getConfigurationParams()