__author__ = 'frieder'
import utils.ClazzLoader
import logic.preproc.minmax
import logic.preproc.bandpass
import logic.preproc.integration
import logic.preproc.std
import logic.preproc.mean
import logic.preproc.variance

class PreProcessingControl(object):
    _instance = None

    def __init__(self, ):
        #TODO: load available algorithms automatically
        self.algorithms = {"minmax":"minmax range","variance":"variance","std":"standard deviation","integration":"Integrate with simpsons rule","bandpass":"bandpass filter"}
        self.selected = None
        self.module_path = "logic.preproc."

    print logic.preproc.minmax.minmax()
    print logic.preproc.bandpass.bandpass()
    print logic.preproc.integration.integration()
    print logic.preproc.std.std()
    print logic.preproc.mean.mean()
    print logic.preproc.variance.variance()


    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(PreProcessingControl, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def getAvailableAlgorithms(self):
        return self.algorithms

    def selectAlgorithm(self, index):
        algo = self.algorithms.keys()[index]
        self.selected = utils.ClazzLoader.loadClazz(self.module_path + algo, algo)

    def preprocData(self, data, params):
        _ins = self.selected()
        needed_params = _ins.getConfigurationParams().keys()
        params2 = [params[p] for p in needed_params]
        print params2
        return _ins.process(data, *params2)

    def getRequiredParameters(self):
        return self.selected().getConfigurationParams()