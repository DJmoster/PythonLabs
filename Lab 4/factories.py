import random
import lorem

from page_utils import Page
from books import Book, ScientificBook, RomanceBook, ManualBook


class BookFactory:
    __RANDOM_SENTENCE_MIN = 1
    __RANDOM_SENTENCE_MAX = 3
    __RANDOM_PAGES_MIN = 5
    __RANDOM_PAGES_MAX = 20

    def create(
            self,
            name: str = 'blank',
            pages: list = None
    ) -> Book:
        if pages is None:
            pages = BookFactory._generate_random_pages(3)

        book = Book(name)
        book.pages = pages

        return book

    @staticmethod
    def create_random(book_obj: Book = Book('blank')):
        book_obj.pages = BookFactory._generate_random_pages(
            random.randint(BookFactory.__RANDOM_PAGES_MIN, BookFactory.__RANDOM_PAGES_MAX)
        )

        return book_obj

    @staticmethod
    def _generate_random_pages(count: int) -> list[Page]:
        res = []
        for i in range(count):
            sentence = lorem.get_sentence(
                random.randint(BookFactory.__RANDOM_SENTENCE_MIN, BookFactory.__RANDOM_SENTENCE_MAX)
            )
            res.append(Page(sentence))

        return res


class ScientificBookFactory(BookFactory):
    def create(
            self,
            name: str = 'blank',
            pages: list = None,
            references: list = None,
            glossary: dict = None
    ) -> ScientificBook:
        if pages is None:
            pages = BookFactory._generate_random_pages(3)

        if references is None:
            references = ['ref1', 'ref2', 'ref3']

        if glossary is None:
            glossary = {'word1': 'desc1', 'word2': 'desc2'}

        scientific_book = ScientificBook(name)
        scientific_book.pages = pages
        scientific_book.references = references
        scientific_book.glossary = glossary

        return scientific_book


class RomanceBookFactory(BookFactory):
    def create(
            self,
            name: str = 'blank',
            pages: list = None,
            characters: dict = None,
    ) -> RomanceBook:
        if pages is None:
            pages = BookFactory._generate_random_pages(3)

        if characters is None:
            characters = {'character1': 'desc1', 'character2': 'desc2'}

        romance_book = RomanceBook(name)
        romance_book.pages = pages
        romance_book.characters = characters

        return romance_book


class ManualBookFactory(BookFactory):
    def create(
            self,
            name: str = 'blank',
            pages: list = None,
            image: str = 'test image.png',
    ) -> ManualBook:
        if pages is None:
            pages = BookFactory._generate_random_pages(3)

        manual_book = ManualBook(name)
        manual_book.pages = pages
        manual_book.image = image

        return manual_book

