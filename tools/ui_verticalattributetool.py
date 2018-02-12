# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

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

class Ui_VerticalAttributeTool(object):
    def setupUi(self, AttributeViever):
        AttributeViever.setObjectName(_fromUtf8("AttributeViever"))
        AttributeViever.setWindowModality(QtCore.Qt.ApplicationModal)
        AttributeViever.resize(245, 420)

        self.atrTab = QtGui.QTabWidget(AttributeViever)
        self.atrTab.setGeometry(QtCore.QRect(0, 0, 235, 360))
        self.atrTab.setObjectName(_fromUtf8("atrTab"))

        self.atrTabPage1 = QtGui.QWidget(AttributeViever)
        self.atrTabPage1.setGeometry(QtCore.QRect(0, 0,200, 360))
        self.atrTabPage1 .setObjectName(_fromUtf8("atrTabPage1"))

        self.atrTabPage2  = QtGui.QWidget(AttributeViever)
        self.atrTabPage2.setGeometry(QtCore.QRect(0, 0,245, 360))
        self.atrTabPage2.setObjectName(_fromUtf8("atrTabPage2"))

        self.atrTable1 = QtGui.QColumnView(AttributeViever)
        self.atrTable1.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.atrTable1.setObjectName(_fromUtf8("atrColumnView1"))

        self.atrTable2 = QtGui.QColumnView(AttributeViever)
        self.atrTable2.setGeometry(QtCore.QRect(30, 30, 50, 50))
        self.atrTable2.setObjectName(_fromUtf8("atrColumnView2"))


        self.btnOK = QtGui.QPushButton(AttributeViever)
        self.btnOK.setGeometry(QtCore.QRect(180, 360, 50, 50))
        self.btnOK.setObjectName(_fromUtf8("btnOK"))


        self.retranslateUi(AttributeViever)
        QtCore.QMetaObject.connectSlotsByName(AttributeViever)

    def retranslateUi(self, AttributeViever):
        AttributeViever.setWindowTitle(_translate("AttributeViever", "Arc Intersection", None))
        self.btnOK.setText(_translate("AttributeViever", "Close", None))

