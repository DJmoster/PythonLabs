import os.path

from .serializable import Serializable
from typing import TypeVar, Generic

T = TypeVar("T")


class CSVDataBase(Generic[T]):

    class DataBaseEmptyException(Exception):
        pass

    class IncorrectIndexException(Exception):
        pass

    class KeyNotExistException(Exception):
        pass

    class IncorrectObjectTypeException(Exception):
        pass

    def __init__(self, obj_class, filename: str, sep: str = ','):
        self.__obj_class = obj_class
        self.__filename = filename
        self.__sep = sep
        self.__data: list[dict] = list()
        self.__unsaved_data: list[dict] = list()

    def __dump(self):
        if len(self.__data) == 0:
            with open(self.__filename, 'w'):
                return

        with open(self.__filename, 'w') as file:
            header_list = ['id']
            header_list.extend(self.__data[0].keys())

            file.write(self.__sep.join(header_list) + '\n')

            for i, v in enumerate(self.__data):
                values_list = [i]
                values_list.extend(v.values())
                values_list = map(str, values_list)

                file.write(self.__sep.join(values_list) + '\n')

    def __load(self):
        temp_data: list[dict] = []
        with open(self.__filename, 'r') as file:
            first = True
            keys = []

            for l in file.readlines():
                if first:
                    keys = l[:-1].split(self.__sep)[1:]
                    first = False

                else:
                    values = l[:-1].split(self.__sep)[1:]
                    obj = dict(zip(keys, values))
                    temp_data.append(obj)

        self.__data.clear()
        self.__data = temp_data

    def fetch(self):
        if os.path.exists(self.__filename):
            self.__load()
        self.__data.extend(self.__unsaved_data)
        self.__dump()
        self.__unsaved_data.clear()

    def get(self, index: int = None) -> list[T] | T:
        self.fetch()
        if index is None:
            return Serializable.convert(self.__obj_class, self.__data)

        self.__check_index(index)
        return Serializable.convert_single(self.__obj_class, self.__data[index])

    def set(self, data: list[T]):
        for i in data:
            if not isinstance(i, self.__obj_class):
                raise CSVDataBase.IncorrectObjectTypeException

        self.__data = list(map(
            lambda o: o.serialize(),
            data
        ))
        self.__dump()

    def add(self, obj: T):
        if not isinstance(obj, self.__obj_class):
            raise CSVDataBase.IncorrectObjectTypeException

        self.__unsaved_data.append(obj.serialize())
        self.fetch()

    def remove(self, index: int):
        self.__load()
        self.__check_index(index)

        del self.__data[index]
        self.__dump()

    def update(self, index: int, **kwargs):
        self.__load()
        self.__check_index(index)

        for k in kwargs.keys():
            key = self.__search_data_key(k)
            self.__data[index][key] = kwargs[k]

        self.__dump()

    def search(self, **kwargs) -> list[T]:
        self.fetch()
        self.__check_if_empty()

        res = list(self.__data)
        for k in kwargs.keys():
            key = self.__search_data_key(k)
            res = list(filter(
                lambda obj: kwargs[k].lower() in obj[key].lower(),
                res
            ))

            if len(res) == 0:
                return []

        return Serializable.convert(self.__obj_class, res)

    def sort(self, key: str = None, reverse: bool = False):
        self.__load()
        self.__check_if_empty()

        key = self.__search_data_key(key)

        if key is None:
            sort_key = lambda o: o[list(self.__data[0].keys())[0]]
        else:
            sort_key = lambda o: o[key]

        self.__data = sorted(self.__data, key=sort_key, reverse=reverse)
        self.__dump()

    def unique_count_by(self, key: str) -> dict[str, int]:
        self.__load()
        self.__check_if_empty()

        key = self.__search_data_key(key)
        count_dict = dict()
        for i in self.__data:
            value = i[key]
            if count_dict.get(value) is None:
                count_dict[value] = 1
            else:
                count_dict[value] += 1

        return count_dict

    def __check_if_empty(self):
        if len(self.__data) == 0:
            raise CSVDataBase.DataBaseEmptyException

    def __check_index(self, index):
        if abs(index) >= len(self.__data):
            raise CSVDataBase.IncorrectIndexException

    def __search_data_key(self, key):
        for i in self.__data[0].keys():
            if i.endswith(key):
                return i

        raise CSVDataBase.KeyNotExistException
