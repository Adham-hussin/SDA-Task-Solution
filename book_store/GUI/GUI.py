import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5.QtCore import Qt


#create a main window
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        #add a title
        self.setWindowTitle("Book Store")
        #set grid layout
        self.setLayout(qtw.QGridLayout())
        #change the icon of the app
        self.setWindowIcon(qtg.QIcon('book.svg'))
        #set minimum size
        self.setMinimumSize(1000, 500)
        #change color of the title bar
        self.setStyleSheet("background-color: #2c2c2c;")
        #add a search bar
        self.search_bar = qtw.QLineEdit()
        self.search_bar.setStyleSheet("background-color: #2c2c2c; color: white; border: 1px solid white; border-radius: 5px;")
        #make the search bar position at the top
        self.search_bar.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.search_bar.setFixedHeight(30)

        self.search_bar.setPlaceholderText("Search for a book")
        self.layout().addWidget(self.search_bar)
        #add a filter icon next to the search bar
        self.filter_icon = qtw.QPushButton(qtg.QIcon('filter.svg'), "")
        self.layout().addWidget(self.filter_icon)
        
        


        
        self.show()
        
        
app = qtw.QApplication([])
mw = MainWindow()
#run the app
app.exec_()