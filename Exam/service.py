from Exam.models import Car, Client, Rent


class CarRentalService:
    class IncorrectRentDaysException(Exception):
        pass

    class CarNotAvailableException(Exception):
        pass

    class CarAlreadyExistsException(Exception):
        pass

    class RentNotFoundException(Exception):
        pass

    def __init__(self, cars: list[Car], service_fee: float = 0.1):
        self.__cars = cars
        self.__balance = 0
        self.__rents: list[Rent] = list()
        self.__service_fee = service_fee

    def __check_if_car_is_available(self, car: Car) -> bool:
        return car in self.__cars and car.status != Car.Status.RENTED

    def __calculate_car_price(self, car: Car, rent_days: int) -> float:
        price = car.price * 0.2

        if car.year < 2011:
            price *= 0.5
        if car.horsepower > 180:
            price *= 0.3

        return price * self.__service_fee * rent_days

    def rent(self, client: Client, car: Car, rent_days: int) -> Rent:
        if rent_days <= 0:
            raise CarRentalService.IncorrectRentDaysException

        if not self.__check_if_car_is_available(car):
            raise CarRentalService.CarNotAvailableException

        rent_price = self.__calculate_car_price(car, rent_days)

        self.__balance += client.pay(rent_price)
        rent = Rent(client, car, rent_days)
        car.status = Car.Status.RENTED

        self.__rents.append(rent)
        return rent

    def my_rents(self, client: Client) -> list[Rent]:
        return [rent for rent in self.__rents if rent.client == client]

    def continue_rent(self, rent: Rent, rent_days: int) -> Rent:
        if rent_days <= 0:
            raise CarRentalService.IncorrectRentDaysException

        if rent not in self.__rents:
            raise CarRentalService.RentNotFoundException

        rent_price = self.__calculate_car_price(rent.car, rent_days)

        self.__balance += rent.client.pay(rent_price)
        new_rent = Rent(rent.client, rent.car, (rent.days_left + rent_days))

        self.__rents.remove(rent)
        self.__rents.append(new_rent)

        return new_rent

    def add_new_car(self, car: Car):
        if car not in self.__cars:
            self.__cars.append(car)
        else:
            raise CarRentalService.CarAlreadyExistsException

    @property
    def cars(self) -> list[Car]:
        return self.__cars

    @property
    def available_cars(self) -> list[Car]:
        return [car for car in self.__cars if car.status != Car.Status.RENTED]
