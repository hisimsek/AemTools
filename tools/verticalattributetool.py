# -*- coding: latin1 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


# Initialize Qt resources from file resources.py
from AemTools import resources

#Import own classes and tools
from verticalattributetoolgui import VerticalAttributeToolGui




class VerticalAttributeTool:
    
        def __init__(self, iface,  toolBar):
            self.iface = iface
            self.canvas = self.iface.mapCanvas()
            self.pointEmitter = QgsMapToolEmitPoint(self.canvas)
            # Create action
            self.act_showArea= QAction(QIcon(":/plugins/AemTools/icons/attr_info.png"), QCoreApplication.translate("ctools", "Select 2 Vertex Points"),  self.iface.mainWindow())
            self.act_showArea.setCheckable(True)
      
            # Connect to signals for button behaviour
            QObject.connect(self.act_showArea, SIGNAL("triggered()"), self.run)
            self.canvas.mapToolSet.connect(self.deactivate)

            toolBar.addAction(self.act_showArea)

            QObject.connect(self.pointEmitter, SIGNAL("canvasClicked(const QgsPoint, Qt::MouseButton)"),
                            self.selectNow)
            self.iface.mapCanvas().setMapTool(self.pointEmitter)
            

        def unsetTool(self):
            mc = self.canvas
            mc.unsetMapTool(self.tool)
            self.act_showArea.setChecked(False)
            QApplication.restoreOverrideCursor()
            
        def deactivate(self):
            self.act_showArea.setChecked(False)
            QApplication.restoreOverrideCursor()

        def selectNow(self, point):
            #QMessageBox.information(None, "Clicked coords", " x: " + str(point.x()) + " Y: " + str(point.y()) )
            mc = self.iface.mapCanvas()
            for layer in mc.layers():
                if layer.type() == layer.VectorLayer:
                    layer.removeSelection()
                    mc.refresh()
            layer = self.iface.activeLayer()

            if not layer or layer.type() != QgsMapLayer.VectorLayer :
                self.iface.messageBar().pushMessage("WARNING:", "Select a vector layer ",
                                                    level=QgsMessageBar.CRITICAL, duration=3)
                return

            width = self.iface.mapCanvas().mapUnitsPerPixel() * 2
            rect = QgsRectangle(point.x() - width,
                                point.y() - width,
                                point.x() + width,
                                point.y() + width)

            rect = self.iface.mapCanvas().mapRenderer().mapToLayerCoordinates(layer, rect)
            layer.select(rect,True)
            for elem in layer.selectedFeatures():
                flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint  # QgisGui.ModalDialogFlags
                self.ctrl = VerticalAttributeToolGui(self.iface.mainWindow(),  flags)
                self.ctrl.initGui()
                self.ctrl.show()

        def run(self):
            self.canvas.setMapTool(self.pointEmitter)
            self.act_showArea.setChecked(True)
            self.iface.messageBar().pushMessage("INFO:", "Select a vector layer and then click on the geometry to get attributes",
                                            level=QgsMessageBar.INFO)
            QApplication.instance().setOverrideCursor(Qt.ArrowCursor)



