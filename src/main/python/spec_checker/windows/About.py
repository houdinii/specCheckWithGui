# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutBox(object):
    def setupUi(self, AboutBox):
        AboutBox.setObjectName("AboutBox")
        AboutBox.resize(400, 300)
        AboutBox.setModal(True)
        self.verticalLayoutWidget = QtWidgets.QWidget(AboutBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 29, 353, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblAppTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblAppTitle.setFont(font)
        self.lblAppTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAppTitle.setObjectName("lblAppTitle")
        self.verticalLayout.addWidget(self.lblAppTitle)
        self.lblAuthor = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.lblAuthor.setFont(font)
        self.lblAuthor.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAuthor.setObjectName("lblAuthor")
        self.verticalLayout.addWidget(self.lblAuthor)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.lblLicense = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblLicense.setWordWrap(True)
        self.lblLicense.setObjectName("lblLicense")
        self.verticalLayout.addWidget(self.lblLicense)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutBox)
        self.buttonBox.accepted.connect(AboutBox.accept)
        self.buttonBox.rejected.connect(AboutBox.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutBox)

    def retranslateUi(self, AboutBox):
        _translate = QtCore.QCoreApplication.translate
        AboutBox.setWindowTitle(_translate("AboutBox", "About SpecChecker"))
        self.lblAppTitle.setText(_translate("AboutBox", "SpecChecker V.0.1.0"))
        self.lblAuthor.setText(_translate("AboutBox", "Written By: Brian Barnes (AKA Houdinii)"))
        self.lblLicense.setText(_translate("AboutBox", "Licensed under: (Insert very lenient and broad open source license here)"))

