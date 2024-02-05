# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'route.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Routefor1(object):
    def setupUi(self, Routefor1):
        Routefor1.setObjectName("Routefor1")
        Routefor1.setEnabled(True)
        Routefor1.resize(673, 522)
        self.Route1 = QtWidgets.QWidget(Routefor1)
        self.Route1.setObjectName("Route1")
        self.gridLayout = QtWidgets.QGridLayout(self.Route1)
        self.gridLayout.setObjectName("gridLayout")
        self.outputResult = QtWidgets.QTextEdit(self.Route1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputResult.sizePolicy().hasHeightForWidth())
        self.outputResult.setSizePolicy(sizePolicy)
        self.outputResult.setMinimumSize(QtCore.QSize(150, 300))
        self.outputResult.setObjectName("outputResult")
        self.gridLayout.addWidget(self.outputResult, 2, 2, 1, 1)
        self.backButton = QtWidgets.QPushButton(self.Route1)
        self.backButton.setMaximumSize(QtCore.QSize(100, 12312321))
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.routeLabel = QtWidgets.QLabel(self.Route1)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.routeLabel.setFont(font)
        self.routeLabel.setObjectName("routeLabel")
        self.verticalLayout.addWidget(self.routeLabel)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.startLabel = QtWidgets.QLabel(self.Route1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLabel.sizePolicy().hasHeightForWidth())
        self.startLabel.setSizePolicy(sizePolicy)
        self.startLabel.setMinimumSize(QtCore.QSize(5, 30))
        self.startLabel.setObjectName("startLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.startLabel)
        self.endLabel = QtWidgets.QLabel(self.Route1)
        self.endLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.endLabel.setObjectName("endLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.endLabel)
        self.FindButton = QtWidgets.QPushButton(self.Route1)
        self.FindButton.setMinimumSize(QtCore.QSize(100, 100))
        self.FindButton.setObjectName("FindButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.FindButton)
        self.endInput = QtWidgets.QPlainTextEdit(self.Route1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endInput.sizePolicy().hasHeightForWidth())
        self.endInput.setSizePolicy(sizePolicy)
        self.endInput.setMinimumSize(QtCore.QSize(50, 40))
        self.endInput.setMaximumSize(QtCore.QSize(500, 50))
        self.endInput.setObjectName("endInput")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.endInput)
        self.startInput = QtWidgets.QPlainTextEdit(self.Route1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startInput.sizePolicy().hasHeightForWidth())
        self.startInput.setSizePolicy(sizePolicy)
        self.startInput.setMinimumSize(QtCore.QSize(50, 40))
        self.startInput.setMaximumSize(QtCore.QSize(500, 50))
        self.startInput.setObjectName("startInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.startInput)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 2)
        Routefor1.setCentralWidget(self.Route1)
        self.statusbar = QtWidgets.QStatusBar(Routefor1)
        self.statusbar.setObjectName("statusbar")
        Routefor1.setStatusBar(self.statusbar)

        self.retranslateUi(Routefor1)
        QtCore.QMetaObject.connectSlotsByName(Routefor1)

    def retranslateUi(self, Routefor1):
        _translate = QtCore.QCoreApplication.translate
        Routefor1.setWindowTitle(_translate("Routefor1", "One Route"))
        self.backButton.setText(_translate("Routefor1", "Back"))
        self.routeLabel.setText(_translate("Routefor1", "One route"))
        self.startLabel.setText(_translate("Routefor1", "Where would you like to start?"))
        self.endLabel.setText(_translate("Routefor1", "Where would you like to end?"))
        self.FindButton.setText(_translate("Routefor1", "Find Route"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Routefor1 = QtWidgets.QMainWindow()
    ui = Ui_Routefor1()
    ui.setupUi(Routefor1)
    Routefor1.show()
    sys.exit(app.exec_())

