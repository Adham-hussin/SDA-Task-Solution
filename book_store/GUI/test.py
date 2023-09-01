from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Book Store")
        MainWindow.resize(860, 660)
        MainWindow.setStyleSheet("background-color: #2c2c2c")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(720, 20, 30, 30))
        self.pushButton.setStyleSheet("border-width: 10px;\n"
                                       "border-radius: 15px;\n"
                                       "background-color:#808080;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../search.png"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.searchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QtCore.QRect(20, 20, 689, 30))
        self.searchBar.setAutoFillBackground(False)
        self.searchBar.setStyleSheet("\n"
                                      "border-width: 10px;\n"
                                      "border-radius: 15px;\n"
                                      "background-color:#808080;")
        self.searchBar.setObjectName("searchBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Search for a Book"))

# Execute the code
app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
app.exec_()

#to make a virtual environment run the following commands in the terminal
#pip install virtualenv
#virtualenv venv
#venv\Scripts\activate