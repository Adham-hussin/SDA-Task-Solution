"""
author: Adham Hussin

This file contains the Section class

Private Members:
    title: string (passed to the constructor)
    books: list of Book objects (filled by a public method)

Public Methods:
    get_title: it returns the title of the section.
    add_book: it adds a Book to the books list defined above.
    search_book_by_title: it searches for a book in the book list by its title.
    search_book_by_author: it searches for all books in the book list by the author.
    delete_book: it deletes a book from the book list using its title.
    show_books: it prints all the books in the section.
    get_books: it returns the books of the section.
"""
from book import book 
from typing import List

class section:
    def __init__(self, title):
        self.__title = title
        self.__books:List[book] = []

    def get_title(self):
        return self.__title

    def add_book(self, title, author, cost):
        self.__books.append(book(title, author, cost))

    def search_book_by_title(self, title):
        temp: List[book] = []
        for bk in self.__books:
            if bk.get_title() in title:
                temp.append(bk)
        return temp

    def search_book_by_author(self, author):
        temp: List[book] = []
        for bk in self.__books:
            if bk.get_author() == author:
                temp.append(bk)
        return temp

    def delete_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                self.__books.remove(book)
                return True
        return False

    def show_books(self):
        for book in self.__books:
            print(book.get_title())
            print(book.get_author())
            print(book.get_cost())
            print("")

    def get_books(self):
        return self.__books