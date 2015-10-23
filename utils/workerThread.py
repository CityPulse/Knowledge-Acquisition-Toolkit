class WorkerThread():
    pass
# from PyQt4.QtCore import QThread, SIGNAL
#
# __author__ = 'daniel'
#
# class WorkerThread( QThread ):
#     def __init__( self, parentThread):
#         QThread.__init__( self, parentThread )
#     def run( self ):
#         self.running = True
#         success = self.doWork()
#         self.emit( SIGNAL( "jobFinished( PyQt_PyObject )" ), success )
#     def stop( self ):
#         self.running = False
#         pass
#     def doWork( self ):
#         return True
#     def cleanUp( self):
#         pass
#
# class CounterThread(WorkerThread):
#     def __init__(self, parentThread):
#         WorkerThread.__init__(self, parentThread)
#     def doWork(self):
#         target = 100000000
#         stepP= target/100
#         stepS=target/10000
#         self.emit( SIGNAL( "primaryText( PyQt_PyObject )" ), "Primary" )
#         self.emit( SIGNAL( "secondaryText( PyQt_PyObject )" ), "Secondary" )
#         self.emit( SIGNAL( "primaryRange( PyQt_PyObject )" ), ( 0, 100 ) )
#         self.emit( SIGNAL( "secondaryRange( PyQt_PyObject )" ), ( 0, 100 ) )
#         count = 0
#         while count < target:
#             if count % stepP == 0:
#                 self.emit( SIGNAL( "primaryValue( PyQt_PyObject )" ), int(count / stepP) )
#             if count % stepS == 0:
#                 self.emit( SIGNAL( "secondaryValue( PyQt_PyObject )" ), count % stepP / stepS )
#             if not self.running:
#                 return False
#             count += 1
#         return True