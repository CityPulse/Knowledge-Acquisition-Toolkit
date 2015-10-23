__author__ = 'frieder'
import utils.ClazzLoader


class RepresentationControl(object):
    _instance = None

    def __init__(self, ):
        #TODO: load available algorithms automatically
        self.algorithms = {"rdf": " Linked Semantic Web representation "}
        self.selected = None
        self.module_path = "logic.representation."

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RepresentationControl, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def getAvailableAlgorithms(self):
        return self.algorithms

    def selectAlgorithm(self, index):
        algo = self.algorithms.keys()[index]
        self.selected = utils.ClazzLoader.loadClazz(self.module_path + algo, algo)

    def represent(self, data, params):
        _ins = self.selected()
        needed_params = _ins.getConfigurationParams().keys()
        params2 = [params[p] for p in needed_params]
        return _ins.process(data, *params2)

    def getRequiredParameters(self):
        return self.selected().getConfigurationParams()
