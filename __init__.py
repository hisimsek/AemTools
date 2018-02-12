from AemTools import AemTools
from PyQt4.QtCore import *

def name():
    return "AemTools"

def description():
    return QCoreApplication.translate("init", "This is a AEM Plugin")

def version():
    return "0.1.0"

def qgisMinimumVersion():
    return "2.0"

def qgisMaximumVersion():
    return "2.99"

def authorName():
    return "Halil ibrahim Simsek"

def icon():
	return "icons/main.png"

def classFactory(iface):
    return AemTools(iface)
