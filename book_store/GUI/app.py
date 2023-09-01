import random
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path[0:0] = ['D:/Personal/SDA-Task-Solution/book_store/classes']
from library import library

lib:library = library("Book Store")



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ############################## Main Window #########################################

        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../book.svg"))
        MainWindow.setWindowIcon(icon)
        MainWindow.resize(1080, 720)
        MainWindow.setStyleSheet("background-color: #2c2c2c")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        ############################## Central Widget #########################################
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        mainCentralWidget(self,MainWindow)


        ############################## Grid Layout #########################################

        
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        mainGrid(self)



        ############################## Grid Layout Items #########################################


        ############################## Search Bar #########################################
        

        self.searchBar = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setAutoFillBackground(False)
        self.searchBar.setStyleSheet("\n"
                                     "border-width: 10px;\n"
                                     "border-radius: 10px;\n"
                                     "background-color:#808080;")
        self.searchBar.setClearButtonEnabled(False)
        self.searchBar.setObjectName("searchBar")
        self.gridLayout.addWidget(self.searchBar, 0, 0, 1, 1)
        


        ############################## Filter Button ######################################

        self.filterButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.filterButton.setEnabled(True)
        self.filterButton.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
        self.filterButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../filter.svg"))
        self.filterButton.setIcon(icon)
        self.filterButton.setIconSize(QtCore.QSize(25, 25))
        self.filterButton.setObjectName("filterButton")
        self.gridLayout.addWidget(self.filterButton, 0, 2, 1, 1)
        self.filterButton.clicked.connect(lambda: self.sideBar.show())


        ############################## Search Button ######################################

        self.searchButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.searchButton.setEnabled(True)
        self.searchButton.setStyleSheet("border-width: 10px;\n"
                                      "border-radius: 10px;\n"
                                      "background-color:#808080;")
        self.searchButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../search.png"))
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QtCore.QSize(25, 25))
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)
        self.searchButton.clicked.connect(lambda: onSearchFilterChanged())


        ############################## List View #########################################

        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidget.setStyleSheet("\n"
                                          "border-width: 10px;\n"
                                                "border-radius: 15px;\n"
                                                "background-color:#808080;")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)
        

        ############################## List View Layout #########################################

        self.listWidgetLayout = QtWidgets.QVBoxLayout()
        self.listWidgetLayout.setContentsMargins(50, 50, 50, 50)
        self.listWidgetLayout.setSpacing(20)
        self.listWidgetLayout.setObjectName("listWidgetLayout")
        self.listWidget.setLayout(self.listWidgetLayout)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel) #scroll smoothly
        self.listWidget.setMovement(QtWidgets.QListView.Static) #disable drag and drop
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust) #resize the items when the window is resized
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom) #make the items appear from top to bottom
        

        ############################## List View Items #########################################

        items = []
        secs = lib.get_sections()
        secsNames = [sec.get_title() for sec in secs]
        authors = set()
        # add books to the list view
        for sec in secs:
                for bk in sec.get_books():
                        authors.add(bk.get_author())
                        bookName = QtWidgets.QListWidgetItem()
                        bookName.setFont(QtGui.QFont("Arial", 20))
                        bookDetails = QtWidgets.QListWidgetItem()
                        bookDetails.setFont(QtGui.QFont("Arial", 15))
                        buyButton = QtWidgets.QListWidgetItem()
                        items.append(bookName)
                        bookName.setBackground(QtGui.QColor(255, 255, 255, 0))
                        button = QtWidgets.QPushButton()
                        button.setText("Buy")
                        button.setStyleSheet("QPushButton\n"
                                        "{\n"
                                        "background-color : #202020;\n"
                                        "border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "color: white;\n"
                                        "font-size: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover\n"
                                        "{\n"
                                        "background-color : #404040;\n"
                                        "}\n"
                                        "QPushButton:pressed\n"
                                        "{\n"
                                        "background-color : #404040;\n"
                                        "}"
                                        )
                        bookDetails.setBackground(QtGui.QColor(255, 255, 255, 50))
                        bookName.setText("      "+ str(bk.get_title()))
                        bookDetails.setText("              Author: "+bk.get_author()+"\n              Section: "+sec.get_title()+"\n              Price: "+str(bk.get_cost())+" EGP")
                        bookName.setSizeHint(QtCore.QSize(200, 100))
                        bookDetails.setSizeHint(QtCore.QSize(200, 200))
                        self.listWidget.addItem(bookName)
                        self.listWidget.addItem(bookDetails)
                        self.listWidget.addItem(buyButton)
                        self.listWidget.setItemWidget(buyButton, button) #this line makes the button appear in the list view
                        bookDetails.setHidden(True)
                        buyButton.setHidden(True)
                        #make a signal for the button
                        button.clicked.connect(lambda: onBuyClick(self))
                        
        self.listWidget.itemClicked.connect(lambda: onBookClick(self.listWidget.currentItem()))
        self.listWidget.itemDoubleClicked.connect(lambda: onBookDoubleClick(self.listWidget.currentItem()))


        ############################## Buy #########################################
        invoiceNumber:int = 0
        def onBuyClick(self):

                #docker window
                self.buyWindow = QtWidgets.QDockWidget()
                self.buyWindow.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
                self.buyWindow.setFloating(True)
                self.buyWindow.setFixedWidth(400)
                self.buyWindow.setFixedHeight(200)
                self.buyWindow.setWindowTitle("Checkout")
                self.buyWindow.setStyleSheet("background-color: #3c3c3c;color:white;font-size:20px;")



                #central widget to add grid to it
                self.buyWindowCentralwidget = QtWidgets.QWidget(self.buyWindow)
                self.buyWindowCentralwidget.setObjectName("buyWindowCentralwidget")
                self.buyWindowCentralwidget.setStyleSheet("background-color: #2c2c2c")

                #create a grid layout
                self.buyWindowGridLayout = QtWidgets.QGridLayout(self.buyWindowCentralwidget)
                self.buyWindowGridLayout.setContentsMargins(10, 10, 10, 10)
                self.buyWindowGridLayout.setSpacing(20)
                self.buyWindowGridLayout.setObjectName("buyWindowGridLayout")

                #create an input field for the name and add it to the grid layout
                self.nameInput = QtWidgets.QLineEdit(self.buyWindowCentralwidget)
                self.nameInput.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.nameInput.setObjectName("nameInput")
                self.nameInput.setPlaceholderText("Name")
                self.buyWindowGridLayout.addWidget(self.nameInput, 0, 0, 1, 1)

                #create an input field for the address and add it to the grid layout
                self.addressInput = QtWidgets.QLineEdit(self.buyWindowCentralwidget)
                self.addressInput.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.addressInput.setObjectName("addressInput")
                self.addressInput.setPlaceholderText("Address")
                self.buyWindowGridLayout.addWidget(self.addressInput, 0, 1, 1, 1)

                #create a label for the price and add it to the grid layout
                self.priceLabel = QtWidgets.QLabel(self.buyWindowCentralwidget)
                self.priceLabel.setObjectName("priceLabel")
                self.priceLabel.setStyleSheet("color: white;\n")
                self.priceLabel.setText("Price: "+str(self.listWidget.item(self.listWidget.row(self.listWidget.currentItem())-1).text()).split("Price: ")[1])
                self.buyWindowGridLayout.addWidget(self.priceLabel, 1, 0, 2, 1)

                #create a confirm button and add it to the grid layout
                self.confirmButton = QtWidgets.QPushButton(self.buyWindowCentralwidget)
                self.confirmButton.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.confirmButton.setObjectName("confirmButton")
                self.confirmButton.setText("Confirm")
                self.buyWindowGridLayout.addWidget(self.confirmButton, 2, 0, 1, 1)
                

                #create a cancel button and add it to the grid layout
                self.cancelButton = QtWidgets.QPushButton(self.buyWindowCentralwidget)
                self.cancelButton.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.cancelButton.setObjectName("cancelButton")
                self.cancelButton.setText("Cancel")
                self.buyWindowGridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
                self.cancelButton.clicked.connect(lambda: self.buyWindow.close())
                self.buyWindow.setWidget(self.buyWindowCentralwidget)
                self.buyWindow.show()
                self.confirmButton.clicked.connect(lambda: onConfirmClick(self))

                ############################## Confirm #########################################
                def onConfirmClick(self):
                        #if the name and address are not empty then the book is bought and the pop up window closes
                        #if the book is bought then the book is removed from the list view and an invoice txt file is created
                        #if the book is not bought then nothing happens
                        if(self.nameInput.text() != "" and self.addressInput.text() != ""):
                                self.buyWindow.close()
                                soldBookName = self.listWidget.item(self.listWidget.row(self.listWidget.currentItem())-2).text().replace("      ", "")
                                invoice = open("invoices/invoice"+str(random.randint(0, 100000))+".txt", "w+")
                                invoice.write("Name: "+self.nameInput.text()+"\nAddress: "+self.addressInput.text()+"\nBook: "+soldBookName+"\nPrice: "+self.listWidget.item(self.listWidget.row(self.listWidget.currentItem())-1).text().split("Price: ")[1])
                                invoice.close()
                                #items.remove(self.listWidget.row(self.listWidget.currentItem()))
                                self.listWidget.takeItem(self.listWidget.row(self.listWidget.currentItem())-2)
                                self.listWidget.takeItem(self.listWidget.row(self.listWidget.currentItem())-1)
                                self.listWidget.takeItem(self.listWidget.row(self.listWidget.currentItem()))
                                self.listWidget.setCurrentItem(self.listWidget.item(0))
                                lib.sell_book(soldBookName)
                                print(lib.get_profits())
                        else:
                                #add a label that says "Please complete the form" and add it to the grid layout
                                self.errorLabel = QtWidgets.QLabel(self.buyWindowCentralwidget)
                                self.errorLabel.setObjectName("errorLabel")
                                self.errorLabel.setStyleSheet("color: red;\n")
                                self.errorLabel.setText("Please complete the form")
                                self.buyWindowGridLayout.addWidget(self.errorLabel, 3, 0, 1, 2)

                               
                        

        
        ############################## List View Signals #########################################

        def onBookClick(item):
                if (item in items):
                        self.listWidget.item(self.listWidget.row(item)+1).setHidden(False)
                        self.listWidget.item(self.listWidget.row(item)+2).setHidden(False)
                else:
                       return
        
        def onBookDoubleClick(item):
                if (item in items):
                        self.listWidget.item(self.listWidget.row(item)+1).setHidden(True)
                        self.listWidget.item(self.listWidget.row(item)+2).setHidden(True)
                else:
                       return

        ############################## Grid Layout Settings #########################################

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.gridLayoutWidget.sizePolicy().hasHeightForWidth())
        self.gridLayoutWidget.setSizePolicy(sizePolicy)
        

        ############################## Side Bar #########################################

        self.sideBar = QtWidgets.QDockWidget()
        # make the side bar on the right side of the window
        self.sideBar.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
        self.sideBar.setAllowedAreas(
            QtCore.Qt.DockWidgetArea.RightDockWidgetArea)
        self.sideBar.setFloating(True)
        self.sideBar.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.sideBar.setFixedWidth(300)
        self.sideBar.setStyleSheet(
            "background-color: #3c3c3c;color:white;font-size:20px;")
        self.sideBar.setWindowTitle("Filter")
        self.sideBar.hide()
        self.horizontalLayout.addWidget(self.sideBar)

        
        ############################## Side Bar Items #########################################


        ############################## Layout #########################################

        self.verticalLayoutWidget = QtWidgets.QWidget(self.sideBar)
        #set height to window height when the window is resized


        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 300, MainWindow.height()))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")


        ############################## Close Button #########################################

        self.closeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.closeButton.setGeometry(QtCore.QRect(270, 0, 30, 30))
        self.closeButton.setStyleSheet("border-width: 1px;\n")
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../close.png"))
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(25, 25))
        self.closeButton.setObjectName("closeButton")
        # make it change color when hovered or pressed
        self.closeButton.setStyleSheet("QPushButton:hover\n"
                                       "{\n"
                                       "background-color : #808080;\n"
                                       "}\n"
                                       "QPushButton:pressed\n"
                                       "{\n"
                                       "background-color : #808080;\n"
                                       "}")
        self.closeButton.clicked.connect(lambda: self.sideBar.hide())

        ############################## Search Signal #########################################

        def onSearchFilterChanged():
                selectedAuthor = self.filterByAuthor.currentText()
                selectedSection = self.filterBySection.currentText()
                currentText = self.searchBar.text()
                for item in items: #hide all the items first
                        if(self.listWidget.item(self.listWidget.row(item)) != None):
                                self.listWidget.item(self.listWidget.row(item)+1).setHidden(True)
                                self.listWidget.item(self.listWidget.row(item)+2).setHidden(True)
                       
                for item in items: #show the items that match the selected author
                        #check if item is not removed by checking for NoneType
                        if(self.listWidget.item(self.listWidget.row(item)) != None):
                                if(currentText in self.listWidget.item(self.listWidget.row(item)).text() or currentText == ""):
                                        if (selectedAuthor in self.listWidget.item(self.listWidget.row(item)+1).text() or selectedAuthor == "Filter By Author"):
                                                if(selectedSection in self.listWidget.item(self.listWidget.row(item)+1).text() or selectedSection == "Filter By Section"):
                                                        item.setHidden(False)
                                                else:
                                                        item.setHidden(True)
                                        else:
                                                item.setHidden(True)
                                else:
                                        item.setHidden(True)
                                
                """ Implementation didn't work :'(
                searchAuthor = [bk.get_title() for bk in lib.search_book_by_author(selectedAuthor)] if selectedAuthor != "Filter By Author" else [ item.text() for item in items ]
                searchTitle = [bk.get_title() for bk in lib.search_book_by_title(currentText)] if currentText != "" else [ item.text() for item in items ]
                searchSection = [(bk.get_title() for bk in sec.get_books() if sec.get_title() == selectedSection) for sec in secs ] if currentText != "" else [ item.text() for item in items ]
                
                
                searchResult = []

                for sec in secs:
                        for bk in sec.get_books():
                                if(bk.get_title() in searchAuthor and bk in searchTitle and bk in searchSection):
                                        searchResult.append(bk.get_title())
                
                for item in items:
                        if(self.listWidget.item(self.listWidget.row(item)).text() in searchResult):
                                item.setHidden(False)
                        else:
                                item.setHidden(True)"""

                

                
                
                       


        ############################## Filter By Author #########################################

        self.filterByAuthor = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.filterByAuthor.setGeometry(QtCore.QRect(10, 60, 281, 31))
        self.filterByAuthor.setStyleSheet("border-width: 10px;\n"
                                                "border-radius: 10px;\n"
                                                "background-color:#808080;")
        self.filterByAuthor.setObjectName("filterByAuthor")
        self.filterByAuthor.addItem("Filter By Author")
        
        for author in authors:
                self.filterByAuthor.addItem(author)
        
        self.filterByAuthor.currentTextChanged.connect(onSearchFilterChanged)

        
        ############################## Filter By Section #########################################

        self.filterBySection = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.filterBySection.setGeometry(QtCore.QRect(10, 170, 281, 31))
        self.filterBySection.setStyleSheet("border-width: 10px;\n"
                                                "border-radius: 10px;\n"
                                                "background-color:#808080;")
        self.filterBySection.setObjectName("filterBySection")
        self.filterBySection.addItem("Filter By Section")

        for sec in secsNames:
                self.filterBySection.addItem(sec)

        self.filterBySection.currentTextChanged.connect(onSearchFilterChanged)

        
        ############################## Remove Filters #########################################

        self.removeFilters = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.removeFilters.setGeometry(QtCore.QRect(10, 280, 281, 31))
        self.removeFilters.setStyleSheet("border-width: 10px;\n"
                                                "border-radius: 10px;\n"
                                                "background-color:#808080;")
        self.removeFilters.setObjectName("removeFilters")
        self.removeFilters.setText("Remove Filters")
        self.removeFilters.clicked.connect(lambda: self.filterByAuthor.setCurrentIndex(0))
        self.removeFilters.clicked.connect(lambda: self.filterBySection.setCurrentIndex(0))
        

        ############################## Settings #########################################

        self.retranslateUi(MainWindow)
        self.searchBar.returnPressed.connect(self.searchButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.searchBar, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.filterButton)
        MainWindow.setTabOrder(self.filterButton, self.listWidget)



    

    def retranslateUi(self, MainWindow): #made by pyuic5
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BookStore"))
        self.searchBar.setPlaceholderText(
            _translate("MainWindow", "Search for a Book"))

def mainCentralWidget(self,MainWindow):
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

def mainGrid(self):
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1041, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout.setContentsMargins(10, 10, 10, 20)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addWidget(self.gridLayoutWidget)

# Execute the code
app = QtWidgets.QApplication([])
window = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
app.exec_()

# to make a virtual environment run the following commands in the terminal
# pip install virtualenv
# virtualenv venv
# venv\Scripts\activate