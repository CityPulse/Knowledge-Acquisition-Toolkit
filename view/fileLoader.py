# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileLoader.ui'
#
# Created: Fri Feb 22 13:23:48 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

import datetime
import csv

from PyQt4 import QtCore, QtGui, Qwt5
from guiqwt.builder import make
from guiqwt.plot import CurveDialog, PlotManager
import pandas
import numpy as np

import logic.DataFlowControl
#newversion

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

###########Make sure you use self.Form = Form after resize
class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(750, 453)
        self.Form = Form
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 0, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        '''self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(20, 70, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 70, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(180, 70, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))'''
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 110, 581, 251))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.startD = QtGui.QLineEdit(Form)
        self.startD.setGeometry(QtCore.QRect(120, 0, 81, 20))
        self.startD.setObjectName(_fromUtf8("startD"))
        self.endD = QtGui.QLineEdit(Form)
        self.endD.setGeometry(QtCore.QRect(240, 0, 71, 20))
        self.endD.setObjectName(_fromUtf8("endD"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Hint = QtGui.QLabel(Form)
        self.Hint.setGeometry(QtCore.QRect(330, 10, 281, 16))
        self.Hint.setObjectName(_fromUtf8("Hint"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 30, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.pushButton.clicked.connect(self.loadDialog)
        self.pushButton_2.clicked.connect(self.saveDialog)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Load Data", None))
        self.label.setText(_translate("Form", "End", None))
        self.label_2.setText(_translate("Form", "Begin", None))
        self.Hint.setText(_translate("Form", "Enter before loading. To load whole dataset, leave blank", None))
        self.pushButton_2.setText(_translate("Form", "Save", None))

    def loadDialog(self):
        filename = QtGui.QFileDialog.getOpenFileName(self.Form, 'Open File', '.')
        fname = open(filename)
        data = fname.read()
        #self.le.setText(filename)
        do = pandas.read_csv(str(filename), delimiter=",")
        #data = pd.read_csv('C:/Users/se00075/PycharmProjects/Test2/src' + '/' + 'data.csv')
        if (self.startD.text().isEmpty()) & (self.endD.text().isEmpty()):
            d=do
        else:
            do['time_stamp'] = do['time_stamp'].astype('datetime64[ns]')
            st = int(self.startD.text())
            en = int(self.endD.text())
            select = (do['time_stamp'] >= do.time_stamp[0]+datetime.timedelta(days=st-1)) & (do['time_stamp'] < do.time_stamp[0]+datetime.timedelta(days=en))
            d = do[select]
            #d = pandas.read_csv(str(filename), delimiter=",")
            #print d
        ##Lets add clean missing data here

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
       #self.original_data=(self.original_data-self.original_data.mean()) / self.original_data.std()

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

    def saveDialog(self):
        path = QtGui.QFileDialog.getSaveFileName(self.Form, 'Save File', '', 'CSV(*.csv)')
        if not path.isEmpty():
            with open(unicode(path), 'wb') as stream:
                writer = csv.writer(stream)
                [a,b]=self.selected_data.shape
                print(a)
                print(b)
                for row in range(a):
                    rowdata = []
                    for column in range(b):
                        item = self.selected_data.item(row, column)
                        if item is not None:
                            rowdata.append(item)
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)








'''import sys
         app = QtGui.QApplication(sys.argv)
         MainWindow = QtGui.QMainWindow()
         ui = Ui_MainWindow()
         ui.setupUi(MainWindow)
         MainWindow.show()'''

