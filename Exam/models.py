import enum
from datetime import date, timedelta


class Client:
    class NotEnoughFundsException(Exception):
        pass

    def __init__(self, name: str, money: float):
        self.__name = name
        self.__money = money

    @property
    def name(self) -> str:
        return self.__name

    @property
    def money(self) -> float:
        return self.__money

    def pay(self, amount: float):
        if amount > self.__money:
            raise Client.NotEnoughFundsException

        self.__money -= amount
        return amount

    def __str__(self):
        return self.__name


class Car:
    class Status(enum.Enum):
        RENTED = 1
        AVAILABLE = 0

    __LAST_CAR_ID = 0

    def __init__(self, year: int, name: str, horsepower: int, price: float):
        self.__car_id = Car.__LAST_CAR_ID
        Car.__LAST_CAR_ID += 1

        self.__year = year
        self.__name = name
        self.__horsepower = horsepower
        self.__price = price
        self.__status = Car.Status.AVAILABLE

    @property
    def car_id(self) -> int:
        return self.__car_id

    @property
    def year(self) -> int:
        return self.__year

    @property
    def name(self) -> str:
        return self.__name

    @property
    def horsepower(self) -> int:
        return self.__horsepower

    @property
    def price(self) -> float:
        return self.__price

    @property
    def status(self) -> Status:
        return self.__status

    @status.setter
    def status(self, status: Status):
        self.__status = status

    def __str__(self):
        return f'{self.__name}({self.car_id})'


class Rent:
    __LAST_RENT_ID = 0

    def __init__(self, client, car: Car, rent_days: int):
        self.__rent_id = Rent.__LAST_RENT_ID
        Rent.__LAST_RENT_ID += 1

        self.__client = client
        self.__car = car
        self.__end_date = date.today() + timedelta(days=rent_days)

    @property
    def rent_id(self) -> int:
        return self.__rent_id

    @property
    def client(self):
        return self.__client

    @property
    def car(self) -> Car:
        return self.__car

    @property
    def days_left(self) -> int:
        return (self.__end_date - date.today()).days

    def __str__(self):
        return f"Rent ID: {self.__rent_id} | Client: {self.__client} | Car: {self.__car} | Days left: {self.days_left}"
