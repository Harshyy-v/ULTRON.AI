from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(417, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 552, 642))
        self.backgroundLabel.setText("")
        self.backgroundLabel.setPixmap(QtGui.QPixmap("background.png"))  # Set your background image path here
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 50, 417, 50))
        font = QtGui.QFont()
        font.setFamily("Notable")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: white")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.terminalOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.terminalOutput.setGeometry(QtCore.QRect(0, 100, 417, 427))
        self.terminalOutput.setStyleSheet("background: transparent; color: white; border: none;")
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(10)
        self.terminalOutput.setFont(font)
        self.terminalOutput.setReadOnly(True)
        self.terminalOutput.setObjectName("terminalOutput")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ULTRON"))
        self.titleLabel.setText(_translate("MainWindow", "ULTRON"))
