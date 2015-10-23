from PyQt4.QtCore import QObject, SIGNAL
from PyQt4.QtGui import QDialog, QVBoxLayout, QLabel, QProgressBar, QPushButton


__author__ = 'daniel'
#Acknowledgement: code skeleton found from
# http://gis.stackexchange.com/questions/45514/how-do-i-maintain-a-resposive-gui-using-qthread-with-pyqgis
# and adapted for own purpose


class ThreadManagerDialog(QDialog):
    def __init__( self, iface, title="Worker Thread"):
        QDialog.__init__( self, iface)#.mainWindow() )
        self.iface = iface
        self.setWindowTitle(title)
        self.setLayout(QVBoxLayout())
        self.primaryLabel = QLabel(self)
        self.layout().addWidget(self.primaryLabel)
        self.primaryBar = QProgressBar(self)
        self.layout().addWidget(self.primaryBar)
        self.secondaryLabel = QLabel(self)
        self.layout().addWidget(self.secondaryLabel)
        self.secondaryBar = QProgressBar(self)
        self.layout().addWidget(self.secondaryBar)
        self.closeButton = QPushButton("Close")
        self.closeButton.setEnabled(False)
        self.layout().addWidget(self.closeButton)
        self.closeButton.clicked.connect(self.reject)
    def run(self):
        self.runThread()
        self.exec_()
    def runThread( self):
        QObject.connect( self.workerThread, SIGNAL( "jobFinished( PyQt_PyObject )" ), self.jobFinishedFromThread )
        QObject.connect( self.workerThread, SIGNAL( "primaryValue( PyQt_PyObject )" ), self.primaryValueFromThread )
        QObject.connect( self.workerThread, SIGNAL( "primaryRange( PyQt_PyObject )" ), self.primaryRangeFromThread )
        QObject.connect( self.workerThread, SIGNAL( "primaryText( PyQt_PyObject )" ), self.primaryTextFromThread )
        QObject.connect( self.workerThread, SIGNAL( "secondaryValue( PyQt_PyObject )" ), self.secondaryValueFromThread )
        QObject.connect( self.workerThread, SIGNAL( "secondaryRange( PyQt_PyObject )" ), self.secondaryRangeFromThread )
        QObject.connect( self.workerThread, SIGNAL( "secondaryText( PyQt_PyObject )" ), self.secondaryTextFromThread )
        self.workerThread.start()
    def cancelThread( self ):
        self.workerThread.stop()
    def jobFinishedFromThread( self, success ):
        self.workerThread.stop()
        self.primaryBar.setValue(self.primaryBar.maximum())
        self.secondaryBar.setValue(self.secondaryBar.maximum())
        self.emit( SIGNAL( "jobFinished( PyQt_PyObject )" ), success )
        self.closeButton.setEnabled( True )
    def primaryValueFromThread( self, value ):
        self.primaryBar.setValue(value)
    def primaryRangeFromThread( self, range_vals ):
        self.primaryBar.setRange( range_vals[ 0 ], range_vals[ 1 ] )
    def primaryTextFromThread( self, value ):
        self.primaryLabel.setText(value)
    def secondaryValueFromThread( self, value ):
        self.secondaryBar.setValue(value)
    def secondaryRangeFromThread( self, range_vals ):
        self.secondaryBar.setRange( range_vals[ 0 ], range_vals[ 1 ] )
    def secondaryTextFromThread( self, value ):
        self.secondaryLabel.setText(value)
