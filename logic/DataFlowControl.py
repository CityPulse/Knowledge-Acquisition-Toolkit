__author__ = 'frieder'
import pandas


class DataController(object):
    """Entity responsible for all data related tasks such as loading"""
    _instance = None

    def __init__(self, ):
        """Constructor for DataController"""
        print "init"

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataController, cls).__new__(
                cls, *args, **kwargs)
        return cls._instance

    def loadSampleData(self):
        """ Mockup function load data from csv into numpy array

        Args:


        Returns:

        """
        # self.DATA = pandas.read_csv("../data.csv", parse_dates=['YYYY-MM-DD HH:MM:SS'])
        self.DATA = pandas.read_csv("../data.csv")
        self.PIR_DATA = self.DATA["PIR"][:]
        return self.DATA

    #def getCurrentDataFlowObject(self):
#
#        if "PIR_DATA" not in self.__dict__:
#            self.loadSampleData()
#            print "loading full dataset"
#
#        return self.PIR_DATA

    @property
    def originalData(self):
        if "PIR_DATA" not in self.__dict__:
            self.loadSampleData()
            print "loading full dataset"
        return self.PIR_DATA

    @originalData.setter
    def originalData(self,data):
        self.PIR_DATA = data

    @property
    def preprocData(self):
        if "preproc" not in self.__dict__:
            return self.originalData
        return self.preproc

    @preprocData.setter
    def preprocData(self,data):
        self.preproc = data

    @property
    def dimrecprocData(self):
        if "dimrecData" not in self.__dict__:
            return self.preprocData
        return self.dimrecData

    @dimrecprocData.setter
    def dimrecprocData(self,data):
        self.dimrecData = data

    @property
    def featureexData(self):
        if "featureData" not in self.__dict__:
            return self.dimrecprocData
        return self.featureData

    @featureexData.setter
    def featureexData(self,data):
        self.featureData = data

    @property
    def abstractionData(self):
        if "abstraction" not in self.__dict__:
            return self.featureexData
        return self.abstraction

    @abstractionData.setter
    def abstractionData(self,data):
        self.abstraction = data

    @property
    def representData(self):
        return self.representData

    @representData.setter
    def representData(self,data):
        self.representData = data

    def getCurrentLabels(self):
        if "labels" not in self.__dict__:
            return None
        return self.labels

    def setCurrentLabels(self,labels):
        self.labels = labels

    @property
    def params(self):
        return self.param

    @params.setter
    def params(self,data):
        self.param = data