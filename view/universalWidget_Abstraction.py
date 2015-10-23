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
from logic.AbstractionControl import AbstractionControl
from logic.DataFlowControl import DataController
from logic.DimensionalityReduceControl import DimensionalityReduceControl
import os

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
        self.drc = AbstractionControl()
        self.flowData = self.dc.featureexData
        pos = self.drc.getAvailableAlgorithms().keys().index(type)
        self.drc.selectAlgorithm(pos)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(536, 384)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 261, 221, 121))
        if self.dc.getCurrentLabels() is None:
            QtGui.QMessageBox.warning(Form, "No Features Found", "Please select Feature Extraction Method first",
                                      QtGui.QMessageBox.Ok)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(list(set(self.dc.getCurrentLabels()))))

        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 360, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.widget = QtGui.QWidget()
        self.widget.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.dialog = CurveDialog(edit=False, toolbar=False, parent=self.widget)
        self.plot = self.dialog.get_plot()
        self.plot.set_antialiasing(True)
        self.plot.setAxisTitle(Qwt5.Qwt.QwtPlot.xBottom, 'Time')
        self.plot.setAxisTitle(Qwt5.Qwt.QwtPlot.yLeft, 'Value')
        self.manager = PlotManager(self)
        self.manager.add_plot(self.plot)
        ly = QtGui.QVBoxLayout()
        ly.addWidget(QtGui.QLabel(self.widget))
        ly.addWidget(QtGui.QLabel(self.plot))
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
        for it in list(set(self.dc.getCurrentLabels())):
        # item = QtGui.QTableWidgetItem()
        # item.setText(_translate("Form", "Id" + str(c), None))
        # self.tableWidget.setVerticalHeaderItem(c, item)

            item = QtGui.QTableWidgetItem()
            item.setText(str(it))
            self.tableWidget.setItem(c, 0, item)
            print "jiggaboo time", it
            #print it, self.drc.getRequiredParameters()[it]
            item = QtGui.QTableWidgetItem()
            item.setText("State "+str(c))
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
        self.pushButton.setText(_translate("Form", "Markov It!", None))

        Form.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.processor)
        print "jo"

    def processor(self):
        print "in process"
        params = {}
        for i in range(self.tableWidget.rowCount()):
            a = self.tableWidget.item(i, 0)
            b = self.tableWidget.item(i, 1)
            params[str(a.text())] = str(b.text())
        print "params", params
        from logic.abstraction.markov import markov
        p,P = markov().abstract(self.dc.getCurrentLabels(),params)
        self.dc.params = params
        print os.getcwd()
        p2 = QtGui.QPixmap("c:\ccsr.png");
        print p2.width(), p2
        self.label.setPixmap(p2.scaled(self.label.size(), QtCore.Qt.KeepAspectRatio))
        self.dc.abstractionData = (p,P)
        #self.label.update()



