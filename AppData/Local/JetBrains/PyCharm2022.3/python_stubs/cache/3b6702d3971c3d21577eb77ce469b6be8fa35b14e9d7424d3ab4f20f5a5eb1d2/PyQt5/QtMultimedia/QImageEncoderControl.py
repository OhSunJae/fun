# encoding: utf-8
# module PyQt5.QtMultimedia
# from C:\Users\OSJ\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\PyQt5\QtMultimedia.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QMediaControl import QMediaControl

class QImageEncoderControl(QMediaControl):
    """ QImageEncoderControl(parent: QObject = None) """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def imageCodecDescription(self, p_str): # real signature unknown; restored from __doc__
        """ imageCodecDescription(self, str) -> str """
        return ""

    def imageSettings(self): # real signature unknown; restored from __doc__
        """ imageSettings(self) -> QImageEncoderSettings """
        return QImageEncoderSettings

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setImageSettings(self, QImageEncoderSettings): # real signature unknown; restored from __doc__
        """ setImageSettings(self, QImageEncoderSettings) """
        pass

    def supportedImageCodecs(self): # real signature unknown; restored from __doc__
        """ supportedImageCodecs(self) -> List[str] """
        return []

    def supportedResolutions(self, QImageEncoderSettings): # real signature unknown; restored from __doc__
        """ supportedResolutions(self, QImageEncoderSettings) -> Tuple[List[QSize], bool] """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass


