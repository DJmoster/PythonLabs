from MyCSVdb.serializable import Serializable


class Book(Serializable):

    def __init__(self,
                 name: str = None,
                 author: str = None,
                 creation_date: str = None,
                 genre: str = None):
        self.__name = name
        self.__author = author
        self.__creation_date = creation_date
        self.__genre = genre

    def __str__(self):
        return f'{self.__name}: {self.__author}, {self.__creation_date}, {self.__genre}'


class User(Serializable):

    def __init__(self, name: str = None, age: int = None):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'{self.__name}: {self.__age}'