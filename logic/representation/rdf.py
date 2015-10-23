__author__ = 'frieder'

from logic.DataFlowControl import DataController
from rdflib import Graph, URIRef, Literal, BNode, Namespace, RDF


class rdf:
    def process(self, data, params):
        store = Graph()
        store.bind("dc", "http://http://purl.org/dc/elements/1.1/")
        store.bind("ccsr", "http://ccsr.ac.uk/rwdata/0.1/")
        CCSR = Namespace("http://ccsr.ac.uk/rwdata/0.1/")
        self.dc = DataController()

        donna = CCSR["bieber"]
        #store.add((donna,RDF.type,CCSR["beer"]))
        #print self.dc.preprocData
        #print self.dc.dimrecprocData
        #print self.dc.featureexData
        #print self.dc.abstractionData
        #print self.dc.getCurrentLabels()
        for i in params:
            store.add((CCSR[params[i]], RDF.type, CCSR["SensorAbstraction"]))
        import utils.rdfVisualizer
        v = utils.rdfVisualizer.Visualizer(store)
        k = v.graph2dot(True)
        k.write_png("s.png", prog='dot')
        return store



    def getConfigurationParams(self):
        return {"states": None}

#r = rdf()
#g =  r.process(None)
#for s,p,o in g:
#    print ((s,p,o))

#print g.serialize(format="xml")

#import utils.rdfVisualizer
#v = utils.rdfVisualizer.Visualizer(g)
#k = v.graph2dot(True)
#k.write_png("s.png", prog='dot')
