# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MockUp1.ui'
#
# Created: Wed Feb 20 23:55:33 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from view.Ui_PlotWidget_FeatureSet import Ui_PlotWidget_Feature_Set
from view.Ui_PlotWidget_LearningSet import Ui_PlotWidget_Learning_Set
from view.Ui_PlotWidget_ReduceSet import Ui_PlotWidget_Reduce_Set
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 700)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = Ui_PlotWidget_Learning_Set(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 50, 521, 151))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget_2 = Ui_PlotWidget_Reduce_Set(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 280, 521, 151))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 250, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget_3 = Ui_PlotWidget_Feature_Set(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(50, 500, 521, 151))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 470, 121, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 450, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 220, 521, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 130, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 350, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 560, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Raw Data", None))
        self.label_2.setText(_translate("MainWindow", "Reduced Data", None))
        self.label_3.setText(_translate("MainWindow", "Feature Extracted Data", None))
        self.pushButton.setText(_translate("MainWindow", "Load", None))
        self.pushButton_2.setText(_translate("MainWindow", "Reduce", None))
        self.pushButton_3.setText(_translate("MainWindow", "Extract", None))

        MainWindow.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.widget.loadData)
        MainWindow.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.widget_2.loadData)
        MainWindow.connect(self.pushButton_3, QtCore.SIGNAL('clicked()'), self.widget_3.loadData)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
