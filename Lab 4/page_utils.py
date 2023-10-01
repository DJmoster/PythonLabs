class PageCounter:
    _instance = None
    __counter = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    @property
    def pages_count(self) -> int:
        return self.__counter

    def generate_id(self) -> int:
        self.__counter += 1

        return self.__counter


class Page:
    def __init__(self, text: str):
        self.__page_id = PageCounter().generate_id()
        self.__text = text

    def __str__(self):
        return self.__text

    @property
    def page_id(self):
        return self.__page_id

    @property
    def text(self):
        return self.__text
