from os import system
from factories import *


def create_book(factory: BookFactory, name):
    return factory.create(name)


scientific_book = BookFactory.create_random(ScientificBook("Scientific book 2"))
scientific_book.add_reference('Reference 1')
scientific_book.add_reference('Reference 2')
scientific_book.glossary = {'Test1': 'Desc1', 'Test2': 'Desc2'}

books_list = [
    create_book(ScientificBookFactory(), 'Scientific book 1'),
    create_book(RomanceBookFactory(), 'Romance book 1'),
    create_book(ManualBookFactory(), 'Manual book 1'),
    BookFactory.create_random(),
    scientific_book
]

while True:
    system('cls')
    print('Book List: \n')

    for i, v in enumerate(books_list):
        print(f'({i}) {v.name}')

    try:
        number = int(input('Choose number: '))

        system('cls')
        print(books_list[number])
        system('pause')

    except ValueError:
        print('Enter a number not a name !!')
        system('pause')

    except IndexError:
        print('Incorrect book number !!')
        system('pause')