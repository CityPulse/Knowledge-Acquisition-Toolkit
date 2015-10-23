# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'universalWidget.ui'
#
# Created: Thu Feb 21 16:00:50 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, Qwt5
from guiqwt.builder import make
from guiqwt.plot import CurveDialog, PlotManager
from logic.DataFlowControl import DataController
from logic.FeatureExtractionControl import FeatureExtractionControl
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Form(object):
    def __init__(self, type):
        self.dc = DataController()
        self.fec = FeatureExtractionControl()
        self.flowData = self.dc.dimrecprocData
        pos = self.fec.getAvailableAlgorithms().keys().index(type)
        self.fec.selectAlgorithm(pos)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(536, 384)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 261, 221, 121))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.fec.getRequiredParameters()))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 360, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.dialog = CurveDialog(edit=False, toolbar=False, parent=self.widget)
        self.plot = self.dialog.get_plot()
        self.plot.set_antialiasing(True)
        self.plot.setAxisTitle(Qwt5.Qwt.QwtPlot.xBottom, 'Time')
        self.plot.setAxisTitle(Qwt5.Qwt.QwtPlot.yLeft, 'Value')
        self.manager = PlotManager(self)
        self.manager.add_plot(self.plot)
        legend = make.legend('TL')
        self.plot.add_item(legend)
        ly = QtGui.QVBoxLayout()
        ly.addWidget(self.plot)
        self.widget.setLayout(ly)

        #   item = QtGui.QTableWidgetItem()
        #   self.tableWidget.setHorizontalHeaderItem(0, item)
        #   item = QtGui.QTableWidgetItem()
        #   self.tableWidget.setItem(0, 0, item)
        #   item = QtGui.QTableWidgetItem()
        #   self.tableWidget.setItem(0, 1, item)

        #        item = self.tableWidget.horizontalHeaderItem(0)
        #       item.setText(_translate("Form", "Attribute", None))

        c = 0
        for it in self.fec.getRequiredParameters():
        # item = QtGui.QTableWidgetItem()
        # item.setText(_translate("Form", "Id" + str(c), None))
        # self.tableWidget.setVerticalHeaderItem(c, item)

            item = QtGui.QTableWidgetItem()
            item.setText(it)
            self.tableWidget.setItem(c, 0, item)

            print it, self.fec.getRequiredParameters()[it]
            item = QtGui.QTableWidgetItem()
            item.setText(str(self.fec.getRequiredParameters()[it]))
            self.tableWidget.setItem(c, 1, item)

            print c
            c += 1

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "Process", None))
        Form.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.process)

    def process(self):
        params = {}
        for i in range(self.tableWidget.rowCount()):
            a = self.tableWidget.item(i, 0)
            b = self.tableWidget.item(i, 1)
            params[str(a.text())] = int(b.text())
        print "params", params
        outpN = self.tableWidget.item(0, 0)
        #params = {"none": "none", "output_length": outpN}


        r = np.array(range(len(self.dc.dimrecprocData))).reshape(len(self.dc.dimrecprocData), 1)
        s = np.array(self.dc.dimrecprocData).reshape(len(self.dc.dimrecprocData), 1)
        rs = np.hstack((s, s))

        labels = self.fec.extractFeature(rs, params)
        print labels
        self.plot.del_all_items()
        self.plot.replot()
        self.plot.add_item(
            make.curve(range(0, len(self.dc.dimrecprocData)), self.dc.dimrecprocData))

        from guiqwt.styles import AnnotationParam

        i = 0
        i_beg = 0
        i_end = 0
        while i < len(labels):
            cur = labels[i_end]

            if i < len(labels) - 1:
                if labels[i_end + 1] != cur:
                    i_end = i
                    from guiqwt.annotations import AnnotatedRectangle

                    param = AnnotationParam()
                    param.title = str(labels[int(i_beg)])
                    param.show_computations = False

                    anno = AnnotatedRectangle(r[int(i_beg)], self.dc.dimrecprocData[int(i_beg)], int(i_end), self.dc.dimrecprocData[r[int(i_end)]], param) #TODO: y axis scaling
                    self.plot.add_item(anno)
                    i_beg = i_end
                    print "s1"
                else:
                    i_end = i
                    print "s2"
                print "s3"
            print "s4", i_end, len(labels)
            i += 1

        self.rangeSelection = make.range(-2, 2)
        disp0 = make.range_info_label(self.rangeSelection, 'BR', u"x = %.1f +- %.1f cm",
                                      title="Range infos")
        #self.plot.add_item(self.rangeSelection)
        #self.plot.add_item(disp0)
        #self.dc.setCurrentDataFlowObject(self.flowData)
        self.dc.featureexData = self.flowData
        self.dc.setCurrentLabels(labels)
        #ToDo: Check that following line, make property in data controller
        self.dc.dimrecprocData = rs
        self.plot.replot()
