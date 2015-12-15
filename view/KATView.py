# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TabDesign2.ui'
#
# Created: Mon Feb 25 19:23:07 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

# from PyQt4 import QtCore, QtGui
from PyQt4 import QtCore, QtGui
from PyQt4 import *
from view import universalWidget_Reduction, universalWidget_Feature, fileLoader, universalWidget_Abstraction, universalWidget_Preproc, universalWidget_Representation

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
        MainWindow.setObjectName(_fromUtf8("Knowledge Acquisition Toolkit"))
        MainWindow.resize(746, 624)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 150, 611, 431))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidget.setTabsClosable(True) # change 1

#        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 110, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        import logic.PreprocessingControl as ncf
        pc = ncf.PreProcessingControl()
        for k in pc.getAvailableAlgorithms().keys(): self.comboBox.addItem(k)

        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 110, 69, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        import logic.DimensionalityReduceControl as d
        c = d.DimensionalityReduceControl()
        for s in c.getAvailableAlgorithms().keys(): self.comboBox_2.addItem(s)

        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(290, 110, 69, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        import logic.FeatureExtractionControl as f
        fc = f.FeatureExtractionControl()
        for g in fc.getAvailableAlgorithms().keys(): self.comboBox_3.addItem(g)


        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(420, 110, 69, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        import logic.AbstractionControl as acf
        ac = acf.AbstractionControl()
        for k in ac.getAvailableAlgorithms().keys(): self.comboBox_4.addItem(k)

        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 611, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))


        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 51))


        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 90, 121, 16))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 90, 101, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 90, 101, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 90, 61, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_5 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(550, 110, 69, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        import logic.RepresentationControl as rpc
        rc = rpc.RepresentationControl()
        for k in rc.getAvailableAlgorithms().keys(): self.comboBox_5.addItem(k)


        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(550, 90, 81, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.graphicsView = QtGui.QLabel(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(620, 490, 121, 91))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))

        p1 = QtGui.QPixmap("../uni.jpg");

        self.graphicsView.setPixmap(p1.scaled(self.graphicsView.size(), QtCore.Qt.KeepAspectRatio))

        self.graphicsView_2 = QtGui.QLabel(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(620, 390, 121, 91))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))

        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 340, 75, 23))
        p2 = QtGui.QPixmap("../ccsr.jpg");
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.graphicsView_2.setPixmap(p2.scaled(self.graphicsView_2.size(), QtCore.Qt.KeepAspectRatio))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.clear)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        fWid = QtGui.QWidget()
        self.fLoader=fileLoader.Ui_Form()
        self.fLoader.setupUi(fWid)
        self.tabWidget.addTab(fWid,_fromUtf8("File Loader"))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Knowledge Acquisition Toolkit", "Knowledge Acquisition Toolkit", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.label.setText(_translate("MainWindow", "Knowledge Acquisition Toolkit", None))
        self.label_2.setText(_translate("MainWindow", "Pre-Processing", None))
        self.label_4.setText(_translate("MainWindow", "Dimension Reduction", None))
        self.label_5.setText(_translate("MainWindow", "Feature Extraction", None))
        self.label_6.setText(_translate("MainWindow", "Abstraction", None))
        self.label_7.setText(_translate("MainWindow", "Representation", None))
        self.label_8.setText(_translate("MainWindow", "University of Surrey 2015", None))
        self.pushButton.setText(_translate("MainWindow", "Restart", None))
        MainWindow.connect(self.comboBox,QtCore.SIGNAL('activated(QString)'),self.loadPreproc)
        MainWindow.connect(self.comboBox_2,QtCore.SIGNAL('activated(QString)'),self.loadReduction)
        MainWindow.connect(self.comboBox_3,QtCore.SIGNAL('activated(QString)'),self.loadFeature)
        MainWindow.connect(self.comboBox_4,QtCore.SIGNAL('activated(QString)'),self.loadAbstraction)
        MainWindow.connect(self.comboBox_5,QtCore.SIGNAL('activated(QString)'),self.loadRepresentation)
        MainWindow.connect(self.tabWidget,QtCore.SIGNAL('tabCloseRequested(int)'),self.closeTab)

    def loadPreproc(self,type):
        print type
        k = QtGui.QWidget()
        bla = universalWidget_Preproc.Ui_Form(type)
        bla.setupUi(k)
        self.tabWidget.addTab(k, _fromUtf8(type))
        self.tabWidget.setCurrentWidget(k)
        k.update()
        k.show()

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

    def loadAbstraction(self,type):
        print type
        k = QtGui.QWidget()
        bla = universalWidget_Abstraction.Ui_Form(type)
        bla.setupUi(k)
        self.tabWidget.addTab(k, _fromUtf8(type))
        self.tabWidget.setCurrentWidget(k)
        k.update()
        k.show()

    def loadRepresentation(self,type):
        print type
        k = QtGui.QWidget()
        bla = universalWidget_Representation.Ui_Form(type)
        bla.setupUi(k)
        self.tabWidget.addTab(k, _fromUtf8(type))
        self.tabWidget.setCurrentWidget(k)
        k.update()
        k.show()

    def closeTab(self,i):
        self.tabWidget.removeTab(i)

    def clear(self):
        #k = QtGui.QWidget()
        k=0;
        while self.tabWidget.count()!=True:
          self.closeTab(k)

        self.closeTab(0)
        self.tabWidget.setCurrentIndex(0)
        fWid = QtGui.QWidget()
        self.fLoader=fileLoader.Ui_Form()
        self.fLoader.setupUi(fWid)
        self.tabWidget.addTab(fWid,_fromUtf8("File Loader"))


'''if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''

def main():
        import sys
        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
        main()