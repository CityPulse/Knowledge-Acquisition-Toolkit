# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileLoader.ui'
#
# Created: Fri Feb 22 13:23:48 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui, Qwt5
from guiqwt.builder import make
from guiqwt.plot import CurveDialog, PlotManager
import pandas
import numpy as np
import logic.DataFlowControl

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
    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(601, 388)
        self.Form = Form
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        #self.checkBox = QtGui.QCheckBox(Form)
        #self.checkBox.setGeometry(QtCore.QRect(10, 50, 70, 17))
        #self.checkBox.setObjectName(_fromUtf8("checkBox"))
        #self.checkBox_2 = QtGui.QCheckBox(Form)
        #self.checkBox_2.setGeometry(QtCore.QRect(90, 50, 70, 17))
        #self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        #self.checkBox_3 = QtGui.QCheckBox(Form)
        #self.checkBox_3.setGeometry(QtCore.QRect(170, 50, 70, 17))
        #self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 100, 581, 261))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.pushButton.clicked.connect(self.loadDialog)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Load Data", None))
        #self.checkBox.setText(_translate("Form", "CheckBox", None))
        #self.checkBox_2.setText(_translate("Form", "CheckBox", None))
        #self.checkBox_3.setText(_translate("Form", "CheckBox", None))

    def loadDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.Form, 'Open File', '.')
        fname = open(filename)
        data = fname.read()
        #self.le.setText(filename)
        d = pandas.read_csv(str(filename), delimiter=",")
        #print d
        space = 0
        self.checkboxes = []
        for i in d.columns:
            c = QtGui.QCheckBox(self.Form)
            #print space
            c.setGeometry(QtCore.QRect(10 + space, 50, 70, 17))
            c.setText(_fromUtf8(i))
            c.show()
            c.clicked.connect(self.selected)
            self.checkboxes.append(c)
            space += 68
        self.original_data = d

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

        self.widget.show()
        self.Form.update()
        self.Form.repaint()

    def selected(self, state):
        dc = logic.DataFlowControl.DataController()
        from itertools import cycle

        colors = cycle(["r", "g", "b", "y"])
        self.plot.del_all_items()
        selItems = []
        for c in self.checkboxes:
            c.isChecked()
            c.text()
            if c.isChecked():
                selItems.append(str(c.text()))
        self.selected_data = np.array(self.original_data[selItems])
        print "fileLoader self.selected_data.shape", self.selected_data.shape
        x = range(self.selected_data.shape[0])
        for g in selItems:
            k = make.curve(x, np.array(self.original_data[g]), color=colors.next())
            self.plot.add_item(k)
        print "fileLoader current data flow object",self.selected_data
        #dc.setCurrentDataFlowObject(self.selected_data)
        dc.originalData = self.selected_data
        self.Form.repaint()
        self.Form.repaint()
        self.plot.update()
