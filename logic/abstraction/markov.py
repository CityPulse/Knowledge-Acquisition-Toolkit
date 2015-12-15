__author__ = 'Shirin'
import pykov
import pydot

class markov:
    def createChain(self,inputData, fromFile=False):
        if fromFile:
            inputData = pykov.readtrj(inputData)
            #print t
        p, P = pykov.maximum_likelihood_probabilities(inputData, lag_time=1, separator='a')
        #print p #vector
        #print P # chain
        return p, P

    def visualizeChain(self,chain,abstraction, filename="markov.png"):
        graph = pydot.Dot(graph_type='digraph')
        for i in chain:
            #print i,chain[i]
            #edge = pydot.Edge(abstraction[str(i[0])], abstraction[str(i[1])], label=chain[i])
            edge = pydot.Edge(str([(i[0])]), str([(i[1])]), label=round(chain[i],2))
            graph.add_edge(edge)
        graph.write_png(filename)

    def getConfigurationParams(self):
        return {}


    def abstract(self,labels,abstraction):
        p,P=self.createChain(labels)

        self.visualizeChain(P,abstraction)
        return p,P
