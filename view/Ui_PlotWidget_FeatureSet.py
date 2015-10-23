__author__ = 'frieder'
from PyQt4 import QtCore, QtGui, Qwt5
from guiqwt.plot import CurvePlot, PlotManager, CurveDialog
from guiqwt.tools import SelectPointTool
from guiqwt.builder import make
import numpy as np
import logic.DataFlowControl as DataController


class Ui_PlotWidget_Feature_Set(QtGui.QWidget):
    """"""

    def __init__(self, parent=None):
        """Constructor for Ui_PlotWidget"""
        QtGui.QWidget.__init__(self, parent)
        self.setupUi()

    def setupUi(self):
        """loads numpy array

        Args:
            self

        Returns:
            nothing
        """
        #self.plot = CurvePlot(self)
        self.dialog = CurveDialog(edit=False, toolbar=True, parent=self)
        self.plot = self.dialog.get_plot()
        self.plot.set_antialiasing(True)

        #x = np.linspace(-10,10,200)
        #dy = x/100.
        #y = np.sin(np.sin(np.sin(x)))
        #self.plot.add_item(make.curve(x,y))

        self.loadButton = QtGui.QPushButton("Load")
        self.trainButton = QtGui.QPushButton("Train Model")

        ly = QtGui.QVBoxLayout()
        ly.addWidget(self.plot)
        #ly.addWidget(self.loadButton)
        #ly.addWidget(self.trainButton)

        self.plot.setAxisTitle(Qwt5.Qwt.QwtPlot.xBottom, 'Time')
        self.plot.setAxisTitle(Qwt5.Qwt.QwtPlot.yLeft, 'Value')

        self.manager = PlotManager(self)
        self.manager.add_plot(self.plot)
        #self.manager.
        legend = make.legend('TL')
        self.plot.add_item(legend)

        self.setLayout(ly)
        self.move(300, 200)
        self.show()
        self.dataController = DataController.DataController()

    def loadData(self):
        self.trainingData = self.dataController.loadSampleData()
        import logic.dimreduce.paa as PAA

        p = PAA.paa()
        data = p.process(self.trainingData["PIR"][:], 100)

        r = np.array(range(len(data))).reshape(len(data), 1)
        s = np.array(data).reshape(len(data), 1)
        rs = np.hstack((s, s))
        print rs
        import logic.featurex.kmeans as km

        k = km.kmeans()
        labels = k.process(rs, 2)
        print labels
        self.plot.add_item(make.curve(range(0, len(data)), data))
        from guiqwt.styles import AnnotationParam
        i=0
        i_beg = 0
        i_end = 0
        while i < len(labels):
            cur = labels[i_end]

            if  i < len(labels)-1:
                if labels[i_end + 1] != cur:
                    i_end=i
                    from guiqwt.annotations import AnnotatedRectangle
                    param = AnnotationParam()
                    param.title = str(labels[int(i_beg)])
                    param.show_computations = False

                    anno = AnnotatedRectangle(r[int(i_beg)],0.5,r[int(i_end)],0.2, param) #TODO: y axis scaling
                    self.plot.add_item(anno)
                    i_beg=i_end
                    print "s1"
                else:
                    i_end =i
                    print "s2"
                print "s3"
            print "s4",i_end,len(labels)
            i+=1
        #param = AnnotationParam()
        #param.title = "alright"
        #param.show_computations = False


        ##anno = AnnotatedRectangle(0., 1., 1.5, 0.5, param)
        #anno.set_style("plot", "shape/drag")
        #anno.set_style("shape/drag/fill/color", "white")
        #self.plot.add_item(anno)
        #self.rangeSelection = make.range(-2, 2)
        #disp0 = make.range_info_label(self.rangeSelection, 'BR', u"x = %.1f +- %.1f cm",
        #                              title="Range infos")
        #self.plot.add_item(self.rangeSelection)
        #self.plot.add_item(disp0)
        self.plot.replot()

    def trainData(self, string_length, vocab, window_length, clusterN):
        a, b = self.rangeSelection.get_range()
        if a > b:
            a, b = b, a
        print a, b
        print "in widget", int(string_length), int(vocab), int(window_length), int(clusterN)
        self.dataController.trainData(a, b, int(string_length), int(vocab), int(window_length), int(clusterN))
