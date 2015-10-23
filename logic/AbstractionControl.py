__author__ = 'frieder'
import utils.ClazzLoader
import logic.abstraction.markov
# import pysparse

class AbstractionControl(object):
    _instance = None

    def __init__(self, ):
        #TODO: load available algorithms automatically
        self.algorithms = {"markov": "Markov Chain based abstraction"}
        self.selected = None
        self.module_path = "logic.abstraction."
        #print pysparse.__version__
        logic.abstraction.markov.markov().getConfigurationParams()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(AbstractionControl, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def getAvailableAlgorithms(self):
        return self.algorithms

    def selectAlgorithm(self, index):
        algo = self.algorithms.keys()[index]
        self.selected = utils.ClazzLoader.loadClazz(self.module_path + algo, algo)

    def abstract(self,data, abstractions):
        print "in abstraction"

    def getRequiredParameters(self):
        return self.selected().getConfigurationParams()
