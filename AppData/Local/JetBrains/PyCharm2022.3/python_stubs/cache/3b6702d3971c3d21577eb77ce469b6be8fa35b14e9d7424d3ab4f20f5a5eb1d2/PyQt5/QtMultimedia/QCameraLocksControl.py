# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\OSJ\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QCameraLocksControl(QMediaControl):
    """ QCameraLocksControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def lockStatus(self, QCamera_LockType): # real signature unknown; restored from __doc__
        """ lockStatus(self, QCamera.LockType) -> QCamera.LockStatus """
        pass

    def lockStatusChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def searchAndLock(self, Union, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__
        """ searchAndLock(self, Union[QCamera.LockTypes, QCamera.LockType]) """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def supportedLocks(self): # real signature unknown; restored from __doc__
        """ supportedLocks(self) -> QCamera.LockTypes """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unlock(self, Union, QCamera_LockTypes=None, QCamera_LockType=None): # real signature unknown; restored from __doc__
        """ unlock(self, Union[QCamera.LockTypes, QCamera.LockType]) """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


