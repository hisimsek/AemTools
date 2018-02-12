from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

import webbrowser, os
import os.path, sys

# Set up current path.
currentPath = os.path.dirname( __file__ )

#Import own tools
from tools.areascreenertool import AreaScreenerTool
from tools.verticalattributetool import VerticalAttributeTool


class AemTools:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        # Initialise the translation environment.
        userPluginPath = QFileInfo(QgsApplication.qgisUserDbFilePath()).path()+"/python/plugins/AemTools"  
        systemPluginPath = QgsApplication.prefixPath()+"/share/qgis/python/plugins/AemTools"
        locale = QSettings().value("locale/userLocale")
        myLocale = locale[0:2]       
            
        if QFileInfo(userPluginPath).exists():
          pluginPath = userPluginPath+"/i18n/AemTools_"+myLocale+".qm"
        elif QFileInfo(systemPluginPath).exists():
          pluginPath = systemPluginPath+"/i18n/AemTools_"+myLocale+".qm"

        self.localePath = pluginPath
        if QFileInfo(self.localePath).exists():
          self.translator = QTranslator()
          self.translator.load(self.localePath)
          
          if qVersion() > '4.3.3':        
            QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # Add toolbar 
        self.toolBar = self.iface.addToolBar("Tkgm Tools")
        self.toolBar.setObjectName("Tkgm Tools")
        
        self.menu = QMenu()
        self.menu.setTitle( QCoreApplication.translate( "TkgmTools","&TkgmTools" ) )
        
        menu_bar = self.iface.mainWindow().menuBar()
        actions = menu_bar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menu_bar.insertMenu( lastAction, self.menu )

      
        # Get the tools
        self.areascreenertool = AreaScreenerTool(self.iface,  self.toolBar)
        self.verticalattributetool = VerticalAttributeTool(self.iface,  self.toolBar)

    def unload(self):
        # remove toolbar and menubar
        del self.toolBar
        del self.menu
        
        
