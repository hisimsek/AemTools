# -*- coding: latin1 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from ui_verticalattributetool import Ui_VerticalAttributeTool

class VerticalAttributeToolGui(QDialog, QObject, Ui_VerticalAttributeTool):
    MSG_BOX_TITLE = "Arc Intersection"


    closeArcIntersectionGui = pyqtSignal()
    unsetTool = pyqtSignal()

    def __init__(self, parent,  fl):
        QDialog.__init__(self, parent,  fl)
        self.setupUi(self)

    def initGui(self):
      pass

    @pyqtSignature("on_btnOK_clicked()")    
    def on_btnOK_clicked(self):
        self.close()
        

