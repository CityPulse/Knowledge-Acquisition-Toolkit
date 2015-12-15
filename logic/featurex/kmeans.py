__author__ = 'frieder'
import time

import numpy as np
import pylab as pl

from sklearn.cluster import MiniBatchKMeans, KMeans


class kmeans():
    def process(self,data,clusterSize):
        kmeans = KMeans(clusterSize)
        kmeans.fit(data)
        labels = kmeans.labels_
        #TODO I added the clusterer as return value will not work with GUI
        return labels

    def getConfigurationParams(self):
        return {"clusterSize":"2"}



