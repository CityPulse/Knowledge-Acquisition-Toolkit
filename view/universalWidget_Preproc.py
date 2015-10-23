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
from logic.PreprocessingControl import PreProcessingControl

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
        self.prc = PreProcessingControl()
        self.flowData = self.dc.originalData
        pos = self.prc.getAvailableAlgorithms().keys().index(type)
        self.prc.selectAlgorithm(pos)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(536, 384)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 261, 221, 121))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.prc.getRequiredParameters()))

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
        for it in self.prc.getRequiredParameters():
        # item = QtGui.QTableWidgetItem()
        # item.setText(_translate("Form", "Id" + str(c), None))
        # self.tableWidget.setVerticalHeaderItem(c, item)

            item = QtGui.QTableWidgetItem()
            item.setText(it)
            self.tableWidget.setItem(c, 0, item)

            #print it, self.prc.getRequiredParameters()[it]
            item = QtGui.QTableWidgetItem()
            item.setText(str(self.prc.getRequiredParameters()[it]))
            self.tableWidget.setItem(c, 1, item)

           # print c
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
       # print "params",params
        outpN = self.tableWidget.item(0, 0)
        #params = {"none": "none", "output_length": outpN}
        data = self.prc.preprocData(self.flowData, params)

        #self.dc.setCurrentDataFlowObject(data)
        #print data
        self.plot.del_all_items()
        print data
        print type(data)
        self.plot.add_item(make.curve(range(0, len(data)), data))
        self.rangeSelection = make.range(-2, 2)
        disp0 = make.range_info_label(self.rangeSelection, 'BR', u"x = %.1f +- %.1f cm",
                                      title="Range infos")
        #self.plot.add_item(self.rangeSelection)
        #self.plot.add_item(disp0)
        self.plot.replot()
        #self.dc.setCurrentDataFlowObject(data)
        self.dc.preprocData = data
