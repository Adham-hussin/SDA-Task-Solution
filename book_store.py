import sys
sys.path[0:0] = ['./book_store/GUI'] 
sys.path[0:0] = ['./book_store/classes']

from gui import Ui_MainWindow
from library import library
from PyQt5 import QtWidgets

libr:library = library("Book Store")

app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window, libr)
window.show()
app.exec_()