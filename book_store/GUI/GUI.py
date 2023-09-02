import random
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path[0:0] = ['../classes']
from library import library





class Ui_MainWindow(object):
    def setupUi(self, MainWindow, lib:library):
        ############################## Main Window #########################################

        MainWindow.setObjectName("MainWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("book_store/GUI/photos/book.svg"))
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
        MainWindow.setWindowTitle("Book Store")

        ############################## Central Widget #########################################
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        mainCentralWidget(self,MainWindow)


        ############################## Grid Layout #########################################

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        mainGrid(self)


        ############################## Grid Layout Items #########################################
        items = []
        secs = lib.get_sections()
        secsNames = [sec.get_title() for sec in secs]
        ############################## Search Bar #########################################
        
        self.searchBar = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Ignored)
        configSizePolicy(self, sizePolicy)
        configSearchBar(self, sizePolicy, items, secs, secsNames, lib)

        
        ############################## Filter Button ######################################

        self.filterButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        configFilterButton(self)


        ############################## List View #########################################

        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listWidgetLayout = QtWidgets.QVBoxLayout()
        configListView(self)

        
        ############################## List View Items #########################################

        
        
        authors = set()
        addBooks(self, items, secs, authors, lib)

        #Show Book Details               
        self.listWidget.itemClicked.connect(lambda: onBookClick(self.listWidget.currentItem()))
        def onBookClick(item):
                if (item in items):
                        self.listWidget.item(self.listWidget.row(item)+1).setHidden(False)
                        self.listWidget.item(self.listWidget.row(item)+2).setHidden(False)
                else:
                       return
        #Hide Book Details
        self.listWidget.itemDoubleClicked.connect(lambda: onBookDoubleClick(self.listWidget.currentItem()))
        def onBookDoubleClick(item):
                if (item in items):
                        self.listWidget.item(self.listWidget.row(item)+1).setHidden(True)
                        self.listWidget.item(self.listWidget.row(item)+2).setHidden(True)
                else:
                       return
        

        ############################## Search Button ######################################

        self.searchButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        configSearchButton(self, items, secs, secsNames, lib)


        ############################## Side Bar #########################################

        self.sideBar = QtWidgets.QDockWidget()
        configSideBar(self)
        

        ############################## Side Bar Layout #########################################

        self.verticalLayoutWidget = QtWidgets.QWidget(self.sideBar)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        configSideBarLayout(self, MainWindow)
        

        ############################## Close Button #########################################

        self.closeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        configCloseButton(self)
        

        ############################## Filter By Author #########################################

        self.filterByAuthor = QtWidgets.QComboBox(self.verticalLayoutWidget)
        configAuthorFilter(self, items, authors, secs, secsNames, lib)

        
        ############################## Filter By Section #########################################

        self.filterBySection = QtWidgets.QComboBox(self.verticalLayoutWidget)
        configSectionFilter(self, items, secs, secsNames, lib)

        
        ############################## Remove Filters #########################################

        self.removeFilters = QtWidgets.QPushButton(self.verticalLayoutWidget)
        configRemoveFilters(self)

        
        ############################## Settings #########################################
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


def addBooks(self, items, secs, authors, lib):
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
                        button.clicked.connect(lambda: onBuyClick(self, lib))

def configAuthorFilter(self, items, authors, secs, secsNames, lib):
        self.filterByAuthor.setGeometry(QtCore.QRect(10, 60, 281, 31))
        self.filterByAuthor.setStyleSheet("border-width: 10px;\n"
                                                "border-radius: 10px;\n"
                                                "background-color:#808080;")
        self.filterByAuthor.setObjectName("filterByAuthor")
        self.filterByAuthor.addItem("Filter By Author")
        
        for author in authors:
                self.filterByAuthor.addItem(author)
        
        self.filterByAuthor.currentTextChanged.connect(lambda : onSearchFilterChanged(self, items, secs, secsNames, lib))

def configCloseButton(self):
                self.closeButton.setGeometry(QtCore.QRect(270, 0, 30, 30))
                self.closeButton.setStyleSheet("border-width: 1px;\n")
                self.closeButton.setText("")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("book_store/GUI/photos/close.png"))
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

def configFilterButton(self):
        self.filterButton.setEnabled(True)
        self.filterButton.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
        self.filterButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("book_store/GUI/photos/filter.svg"))
        self.filterButton.setIcon(icon)
        self.filterButton.setIconSize(QtCore.QSize(25, 25))
        self.filterButton.setObjectName("filterButton")
        self.gridLayout.addWidget(self.filterButton, 0, 2, 1, 1)
        self.filterButton.clicked.connect(lambda: self.sideBar.show())

def configListView(self):
        self.listWidget.setStyleSheet("\n"
                                          "border-width: 10px;\n"
                                                "border-radius: 15px;\n"
                                                "background-color:#808080;")
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)

        self.listWidgetLayout.setContentsMargins(50, 50, 50, 50)
        self.listWidgetLayout.setSpacing(20)
        self.listWidgetLayout.setObjectName("listWidgetLayout")
        self.listWidget.setLayout(self.listWidgetLayout)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel) #scroll smoothly
        self.listWidget.setMovement(QtWidgets.QListView.Static) #disable drag and drop
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust) #resize the items when the window is resized
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom) #make the items appear from top to bottom

def configRemoveFilters(self):
        self.removeFilters.setGeometry(QtCore.QRect(10, 280, 281, 31))
        self.removeFilters.setStyleSheet("border-width: 10px;\n"
                                                "border-radius: 10px;\n"
                                                "background-color:#808080;")
        self.removeFilters.setObjectName("removeFilters")
        self.removeFilters.setText("Remove Filters")
        self.removeFilters.clicked.connect(lambda: self.filterByAuthor.setCurrentIndex(0))
        self.removeFilters.clicked.connect(lambda: self.filterBySection.setCurrentIndex(0))

def configSearchBar(self, sizePolicy, items, secs, secsNames, lib):
        self.searchBar.setFont(QtGui.QFont("Arial", 10))
        self.searchBar.setPlaceholderText("Search for a book")
        self.searchBar.setSizePolicy(sizePolicy)
        self.searchBar.setAutoFillBackground(False)
        self.searchBar.setStyleSheet("\n"
                                     "border-width: 10px;\n"
                                     "border-radius: 10px;\n"
                                     "background-color:#808080;")
        self.searchBar.setClearButtonEnabled(False)
        self.searchBar.setObjectName("searchBar")
        self.searchBar.textChanged.connect(lambda: onSearchFilterChanged(self, items, secs, secsNames, lib))
        self.gridLayout.addWidget(self.searchBar, 0, 0, 1, 1)

def configSearchButton(self, items, secs, secsNames, lib):
        self.searchButton.setEnabled(True)
        self.searchButton.setStyleSheet("border-width: 10px;\n"
                                      "border-radius: 10px;\n"
                                      "background-color:#808080;")
        self.searchButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("book_store/GUI/photos/search.svg"))
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QtCore.QSize(25, 25))
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)
        self.searchButton.clicked.connect(lambda: onSearchFilterChanged(self, items, secs, secsNames, lib))
        self.searchBar.returnPressed.connect(self.searchButton.click)

def configSectionFilter(self, items, secs, secsNames, lib):
        self.filterBySection.setGeometry(QtCore.QRect(10, 170, 281, 31))
        self.filterBySection.setStyleSheet("border-width: 10px;\n"
                                                "border-radius: 10px;\n"
                                                "background-color:#808080;")
        self.filterBySection.setObjectName("filterBySection")
        self.filterBySection.addItem("Filter By Section")

        for sec in secsNames:
                self.filterBySection.addItem(sec)

        self.filterBySection.currentTextChanged.connect(lambda: onSearchFilterChanged(self, items,secs, secsNames, lib))

def configSideBar(self):
                self.sideBar.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
                self.sideBar.setAllowedAreas(QtCore.Qt.DockWidgetArea.RightDockWidgetArea)
                self.sideBar.setFloating(True)
                self.sideBar.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
                self.sideBar.setFixedWidth(300)
                self.sideBar.setStyleSheet(
                "background-color: #3c3c3c;color:white;font-size:20px;")
                self.sideBar.setWindowTitle("Filter")
                self.sideBar.hide()
                self.horizontalLayout.addWidget(self.sideBar)

def configSideBarLayout(self, MainWindow):
                self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 30, 300, MainWindow.height()))
                self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
                self.verticalLayout.setContentsMargins(10, 10, 10, 10)
                self.verticalLayout.setSpacing(20)
                self.verticalLayout.setObjectName("verticalLayout")

def configSizePolicy(self, sizePolicy):
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.searchBar.sizePolicy().hasHeightForWidth())

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

def onBuyClick(self, lib):

        def configInvoiceWindow(self):
                self.buyWindow.setFeatures(QtWidgets.QDockWidget.DockWidgetMovable)
                self.buyWindow.setFloating(True)
                self.buyWindow.setFixedWidth(400)
                self.buyWindow.setFixedHeight(200)
                self.buyWindow.setWindowTitle("Checkout")
                self.buyWindow.setStyleSheet("background-color: #3c3c3c;color:white;font-size:20px;")                
                self.buyWindowCentralwidget.setObjectName("buyWindowCentralwidget")
                self.buyWindowCentralwidget.setStyleSheet("background-color: #2c2c2c")
        
        def configInvoiceWindowGrid(self):
                
                self.buyWindowGridLayout.setContentsMargins(10, 10, 10, 10)
                self.buyWindowGridLayout.setSpacing(20)
                self.buyWindowGridLayout.setObjectName("buyWindowGridLayout")

        def configInvoiceNameInput(self):
                self.nameInput.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.nameInput.setObjectName("nameInput")
                self.nameInput.setPlaceholderText("Name")
                self.buyWindowGridLayout.addWidget(self.nameInput, 0, 0, 1, 1)

        def configInvoiceAddressInput(self):
                
                self.addressInput.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.addressInput.setObjectName("addressInput")
                self.addressInput.setPlaceholderText("Address")
                self.buyWindowGridLayout.addWidget(self.addressInput, 0, 1, 1, 1)

        def configInvoicePriceLabel(self):
                
                self.priceLabel.setObjectName("priceLabel")
                self.priceLabel.setStyleSheet("color: white;\n")
                self.priceLabel.setText("Price: "+str(self.listWidget.item(self.listWidget.row(self.listWidget.currentItem())-1).text()).split("Price: ")[1])
                self.buyWindowGridLayout.addWidget(self.priceLabel, 1, 0, 2, 1)

        def configInvoiceConfirmButton(self):
                
                self.confirmButton.setStyleSheet("border-width: 10px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color:#808080;")
                self.confirmButton.setObjectName("confirmButton")
                self.confirmButton.setText("Confirm")
                self.buyWindowGridLayout.addWidget(self.confirmButton, 2, 0, 1, 1)
                

        def configInvoiceCancelButton(self):
                
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

        def onConfirmClick(self):
                if(self.nameInput.text() != "" and self.addressInput.text() != ""):
                        self.buyWindow.close()
                        soldBookName = self.listWidget.item(self.listWidget.row(self.listWidget.currentItem())-2).text().replace("      ", "")
                        invoice = open("book_store/invoices/invoice"+str(random.randint(0, 100000))+".txt", "w+")
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

        self.buyWindow = QtWidgets.QDockWidget()
        self.buyWindowCentralwidget = QtWidgets.QWidget(self.buyWindow)
        configInvoiceWindow(self)
        self.buyWindowGridLayout = QtWidgets.QGridLayout(self.buyWindowCentralwidget)
        self.nameInput = QtWidgets.QLineEdit(self.buyWindowCentralwidget)
        self.addressInput = QtWidgets.QLineEdit(self.buyWindowCentralwidget)
        self.priceLabel = QtWidgets.QLabel(self.buyWindowCentralwidget)
        self.confirmButton = QtWidgets.QPushButton(self.buyWindowCentralwidget)
        self.cancelButton = QtWidgets.QPushButton(self.buyWindowCentralwidget)
        
        configInvoiceWindowGrid(self)
        configInvoiceNameInput(self)
        configInvoiceAddressInput(self)
        configInvoicePriceLabel(self)
        configInvoiceConfirmButton(self)
        configInvoiceCancelButton(self)

def onSearchFilterChanged(self, items, secs, secsNames, lib):
                selectedAuthor = self.filterByAuthor.currentText()
                selectedSection = self.filterBySection.currentText()
                currentText = self.searchBar.text().lower()
                for item in items: #hide all the items details first
                        if(self.listWidget.item(self.listWidget.row(item)) != None):
                                self.listWidget.item(self.listWidget.row(item)+1).setHidden(True)
                                self.listWidget.item(self.listWidget.row(item)+2).setHidden(True)
                       
                allBooks = []
                searchAuthor = []
                searchTitle = []
                searchSection = []
                searchResult = []

                for sec in secs:
                        for bk in sec.get_books():
                                allBooks.append(bk.get_title())

                if(selectedAuthor != "Filter By Author"):
                        foundBooks = lib.search_book_by_author(selectedAuthor)
                        for bk in foundBooks:
                                searchAuthor.append(bk.get_title())
                else:
                        searchAuthor = allBooks

                if(selectedSection != "Filter By Section"):
                        foundBooks = lib.get_sections()[secsNames.index(selectedSection)].get_books()
                        for bk in foundBooks:
                                searchSection.append(bk.get_title())
                else:
                        searchSection = allBooks

                if(currentText != ""):
                        foundBooks = lib.search_book_by_title(currentText)
                        for bk in foundBooks:
                                searchTitle.append(bk.get_title())
                else:
                        searchTitle = allBooks
                
                
                for bk in allBooks:
                        if(bk in searchAuthor and bk in searchSection and bk in searchTitle):
                                searchResult.append(bk)

                for item in items:
                        if(self.listWidget.item(self.listWidget.row(item)) != None):
                                if(self.listWidget.item(self.listWidget.row(item)).text().replace("      ","") in searchResult):
                                        item.setHidden(False)
                                else:
                                        item.setHidden(True)

