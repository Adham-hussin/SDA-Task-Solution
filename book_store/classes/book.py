"""
author: Adham Hussin

This file contains the Book class

Private Members:
    title: string
    author: string
    cost: float

Public Methods:
    get_title: it's responsible of returning the title of the book
    get_author: it's responsible of returning the Author of the book
    get_cost: it's responsible of returning the Cost of the book.
"""
class book:
    def __init__(self, title, author, cost):
        self.__title: str = title
        self.__author: str = author
        self.__cost: float = cost

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_cost(self):
        return self.__cost    
    

