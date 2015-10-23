# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab.ui'
#
# Created: Thu Feb 21 15:17:29 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from view import universalWidget_Reduction, universalWidget_Feature, fileLoader

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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabsClosable(True) #Change 1
        self.tabWidget.setGeometry(QtCore.QRect(60, 110, 611, 431))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        #self.tab_2 = QtGui.QWidget()
        #self.tab_2.setObjectName(_fromUtf8("tab_2"))
        #self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        #self.tab = QtGui.QWidget()
        #self.tab.setObjectName(_fromUtf8("tab"))
        #self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 20, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        import logic.DimensionalityReduceControl as d
        c = d.DimensionalityReduceControl()
        for s in c.getAvailableAlgorithms().keys(): self.comboBox.addItem(s)



        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 20, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))

        import logic.FeatureExtractionControl as f
        fc = f.FeatureExtractionControl()
        for g in fc.getAvailableAlgorithms().keys(): self.comboBox_2.addItem(g)

        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(280, 20, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(380, 20, 69, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        fWid = QtGui.QWidget()
        self.fLoader=fileLoader.Ui_Form()
        self.fLoader.setupUi(fWid)
        self.tabWidget.addTab(fWid,_fromUtf8("File Loader"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        MainWindow.connect(self.comboBox,QtCore.SIGNAL('activated(QString)'),self.loadReduction)
        MainWindow.connect(self.comboBox_2,QtCore.SIGNAL('activated(QString)'),self.loadFeature)
        MainWindow.connect(self.tabWidget,QtCore.SIGNAL('tabCloseRequested(int)'),self.closeTab)

    def loadReduction(self,type):
        print type
        k = QtGui.QWidget()
        bla = universalWidget_Reduction.Ui_Form(type)
        bla.setupUi(k)
        self.tabWidget.addTab(k, _fromUtf8(type))
        self.tabWidget.setCurrentWidget(k)
        k.update()
        k.show()

    def loadFeature(self,type):
        print type
        k = QtGui.QWidget()
        bla = universalWidget_Feature.Ui_Form(type)
        bla.setupUi(k)
        self.tabWidget.addTab(k, _fromUtf8(type))
        self.tabWidget.setCurrentWidget(k)
        k.update()
        k.show()

    def closeTab(self,i):
        self.tabWidget.removeTab(i)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
