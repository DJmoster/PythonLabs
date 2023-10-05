import base64

from page_utils import Page


class Book:

    def __init__(self, name: str):
        self.__name = name
        self.__pages = []

    def __str__(self):
        res = f'Book: {self.__name}\n'

        for i, v in enumerate(self.__pages):
            res += f'Page ({i}): \n{v}\n'

        return res

    @property
    def name(self):
        return self.__name

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages):
        self.__pages = pages

    def add_page(self, page: Page):
        self.__pages.append(page)

    def add_pages(self, pages: list[Page]):
        self.__pages.extend(pages)


class ScientificBook(Book):

    def __init__(self, name: str):
        super().__init__(name)

        self.__references = []
        self.__glossary = {}

    def __str__(self):
        res = super().__str__()

        res += f'\nReferences List:\n'
        for i in self.__references:
            res += f'  {i},\n'

        res += f'\nGlossary: \n'
        for k in self.__glossary.keys():
            res += f'  {k}: {self.__glossary.get(k)}\n'

        return res

    @property
    def references(self):
        return self.__references

    @references.setter
    def references(self, references: list):
        self.__references = references

    def add_reference(self, reference: str):
        self.__references.append(reference)

    def add_references(self, references: list):
        self.__references.extend(references)

    @property
    def glossary(self):
        return self.__glossary

    @glossary.setter
    def glossary(self, glossary: dict):
        self.__glossary = glossary

    @property
    def glossary_keys(self):
        return self.__glossary.keys()

    def glossary_get(self, key: str):
        return self.__glossary.get(key)

    def glossary_add(self, key: str, value: str):
        self.__glossary[key] = value


class RomanceBook(Book):
    def __init__(self, name: str):
        super().__init__(name)

        self.__characters = {}

    def __str__(self):
        res = super().__str__()
        res += '\nCharacters: \n'

        for k in self.__characters.keys():
            res += f'  {k}: {self.__characters.get(k)}\n'

        return res

    @property
    def characters(self):
        return self.__characters

    @characters.setter
    def characters(self, characters: dict):
        self.__characters = characters

    def get_character_desc(self, character: str):
        return self.__characters.get(character)

    def add_character(self, name: str, desc: str):
        self.__characters[name] = desc


class ManualBook(Book):
    def __init__(self, name):
        super().__init__(name)

        self.__image = None

    def __str__(self):
        res = super().__str__()
        res += f'\n Image: {self.__image}'

        return res

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image):
        with open(image, 'rb') as image_file:
            self.__image = base64.b64encode(image_file.read()).decode('ascii')
