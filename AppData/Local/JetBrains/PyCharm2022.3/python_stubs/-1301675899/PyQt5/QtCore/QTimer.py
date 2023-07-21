# encoding: utf-8
# module PyQt5.QtCore
# from C:\Users\OSJ\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QTimer(QObject):
    """ QTimer(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def interval(self): # real signature unknown; restored from __doc__
        """ interval(self) -> int """
        return 0

    def isActive(self): # real signature unknown; restored from __doc__
        """ isActive(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def isSingleShot(self): # real signature unknown; restored from __doc__
        """ isSingleShot(self) -> bool """
        return False

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def remainingTime(self): # real signature unknown; restored from __doc__
        """ remainingTime(self) -> int """
        return 0

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setInterval(self, p_int): # real signature unknown; restored from __doc__
        """ setInterval(self, int) """
        pass

    def setSingleShot(self, bool): # real signature unknown; restored from __doc__
        """ setSingleShot(self, bool) """
        pass

    def setTimerType(self, Qt_TimerType): # real signature unknown; restored from __doc__
        """ setTimerType(self, Qt.TimerType) """
        pass

    def singleShot(self, p_int, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        singleShot(int, PYQT_SLOT)
        singleShot(int, Qt.TimerType, PYQT_SLOT)
        """
        pass

    def start(self, p_int=None): # real signature unknown; restored from __doc__ with multiple overloads
        """
        start(self, int)
        start(self)
        """
        pass

    def stop(self): # real signature unknown; restored from __doc__
        """ stop(self) """
        pass

    def timeout(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, QTimerEvent): # real signature unknown; restored from __doc__
        """ timerEvent(self, QTimerEvent) """
        pass

    def timerId(self): # real signature unknown; restored from __doc__
        """ timerId(self) -> int """
        return 0

    def timerType(self): # real signature unknown; restored from __doc__
        """ timerType(self) -> Qt.TimerType """
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


