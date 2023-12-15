from random import randint
import lorem

from Exam.models import Car
from Exam.service import CarRentalService


class CarRentalServiceFactory:

    @staticmethod
    def __generate_cars():
        res = []
        for _ in range(randint(5, 20)):
            res.append(Car(
                year=randint(2000, 2023),
                name=lorem.get_word(1),
                horsepower=randint(100, 500),
                price=randint(3000, 100000)
            ))

        return res

    @staticmethod
    def create():
        cars = CarRentalServiceFactory.__generate_cars()

        return CarRentalService(cars)
