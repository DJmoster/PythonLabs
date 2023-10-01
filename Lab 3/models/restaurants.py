from models.client_types import Critic
from models.enums import SushiMenu, PizzaMenu, SteakhouseMenu
from models.exceptions import ClientVisitingAnotherRestaurant, IncorrectMenu, IncorrectClient, NeverVisited


class Restaurant:
    def __init__(self, menu):
        self.__menu = menu
        self.__clients_history = set()
        self.__balance = 0
        self.__rating = 0

    def visit(self, client):
        if client.now_visiting is not None:
            raise ClientVisitingAnotherRestaurant("Клієнт не може бути у 2 ресторанах одночасно !!")

        client.now_visiting = self
        self.__clients_history.add(client)

    def leave(self, client):
        if client.now_visiting is not self:
            raise ClientVisitingAnotherRestaurant("Клієнт не може покинути ресторан у якому не перебуває !!")

        client.now_visiting = None

    def order(self, client, menu_position):
        if not isinstance(menu_position, self.__menu):
            raise IncorrectMenu("Ви не можете це замовити в цьому ресторані !!")

        client.wallet.pay(menu_position.value[1])
        self.__balance += menu_position.value[1]

    def rate(self, client, rate_points):
        if type(client) is not Critic:
            raise IncorrectClient("Оцінювати ресторан може тільки критик !!")

        if client not in self.__clients_history:
            raise NeverVisited("Ви не можете оцінити ресторан не відвідавши його !!")

        points = rate_points * client.multiplier
        print(f"Критик оцінив ресторан на {points} балів")

        self.__rating += points

    @property
    def rating(self):
        return self.__rating

    @property
    def menu(self):
        return self.__menu

    @property
    def balance(self):
        return self.__balance


class SushiRestaurant(Restaurant):
    def __init__(self):
        super().__init__(SushiMenu)

    def visit(self, client):
        super().visit(client)
        print(f"Клієнт {client.name} відвідує суші ресторан")

    def order(self, client, menu_position):
        super().order(client, menu_position)
        print(f"Клієнт {client.name} замовив {menu_position.value[0]} в суші ресторані")

    def leave(self, client):
        super().leave(client)
        print(f"Клієнт {client.name} покинув суші ресторан")


class PizzaRestaurant(Restaurant):
    def __init__(self):
        super().__init__(PizzaMenu)

    def visit(self, client):
        super().visit(client)
        print(f"Клієнт {client.name} відвідує піцерію")

    def order(self, client, menu_position):
        super().order(client, menu_position)
        print(f"Клієнт {client.name} замовив {menu_position.value[0]} в піцерії")

    def leave(self, client):
        super().leave(client)
        print(f"Клієнт {client.name} покинув піцерію")


class SteakhouseRestaurant(Restaurant):
    def __init__(self):
        super().__init__(SteakhouseMenu)

    def visit(self, client):
        super().visit(client)
        print(f"Клієнт {client.name} відвідує стейк хаус")

    def order(self, client, menu_position):
        super().order(client, menu_position)
        print(f"Клієнт {client.name} замовив {menu_position.value[0]} в стейк хаусі")

    def leave(self, client):
        super().leave(client)
        print(f"Клієнт {client.name} покинув стейкхаус")
