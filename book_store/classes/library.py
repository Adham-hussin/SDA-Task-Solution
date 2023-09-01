"""
author: Adham Hussin

This file contains the Library class

Private Members:
    title: string (passed to the constructor)
    sections: list of Section objects (filled by a private method)
    profits: float (updated by a public method)

Public Methods:
    search_book_by_title: it searches for a book in all sections by its title.
    search_book_by_author: it searches for all books in all sections by the author.
    sell_book: it deletes a book from the book list using its title and add the book cost to profit.
    get_profits: it returns the profits of the library.
    get_sections: it returns the sections of the library.

Private Methods:
    __add_section: it adds a section to the sections list defined above.
    __import_books: it imports the books from the json file and add them to the sections list.
"""
from typing import List
from section import section
from book import book
import json


class library:
    def __init__(self, title): 
        self.__title: str = title
        self.__sections: List[section] = []
        self.__profits: float = 0
        self.__import_books()

                       
    def __add_section(self, sectionTitle: str):
        newSection: section = section(sectionTitle)
        self.__sections.append(newSection)

    def __import_books(self):
        with open('books.json', 'r') as db:
            data: dict = json.load(db)
        for book in data:
            exists: bool = False
            for sec in self.__sections:
                if data[book]['section'] == sec.get_title():
                    exists = True
                    break
            if exists == False:
                self.__add_section(data[book]['section'])
            for sec in self.__sections:
                if data[book]['section'] == sec.get_title():
                    sec.add_book(book, data[book]['author'], data[book]['cost'])
                    break

    def search_book_by_title(self, bookTitle: str):
        temp: List[book] = []
        for sec in self.__sections:
            temp.extend(sec.search_book_by_title(bookTitle))
        return temp
    
    def search_book_by_author(self, author: str):
        temp: List[book] = []
        for sec in self.__sections:
            temp.extend(sec.search_book_by_author(author))
        return temp
    
    def sell_book(self, bookTitle: str):
        sold: List[book] = self.search_book_by_title(bookTitle)
        if len(sold) != 1:
            return False
        else:
            self.__profits += sold[0].get_cost()
            i: int = 0
            while self.__sections[i].delete_book(bookTitle) == False: #could've used a for loop but Dr. Howaida said never use 'break' within a for loop 😂 or else u'll get a zero 😐
                i += 1
    
    def get_profits(self):
        return self.__profits
    
    def get_sections(self):
        return self.__sections
    
        
    


    