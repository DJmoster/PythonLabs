from models.payment_methods import Wallet


class Client:
    def __init__(self, name, wallet: Wallet):
        self.__name = name
        self.__wallet = wallet
        self.__now_visiting = None

    @property
    def now_visiting(self):
        return self.__now_visiting

    @now_visiting.setter
    def now_visiting(self, restaurant):
        self.__now_visiting = restaurant

    @property
    def wallet(self):
        return self.__wallet

    @property
    def name(self):
        return self.__name


class Critic(Client):
    def __init__(self, name, wallet: Wallet, multiplier):
        super().__init__(name, wallet)
        self.__multiplier = multiplier

    @property
    def multiplier(self):
        return self.__multiplier
