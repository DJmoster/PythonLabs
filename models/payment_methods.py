from models.exceptions import InsufficientBalanceException


class Wallet:
    def __init__(self, balance: int):
        self.__balance: int = balance

    def pay(self, amount: int):
        if self.__balance < amount:
            raise InsufficientBalanceException("Недостатньо коштів на рахунку !!")

        self.__balance -= amount

    @property
    def balance(self):
        return self.__balance


class Cash(Wallet):
    def pay(self, amount: int):
        super().pay(amount)

        print(f"Ви оплатили {amount} готівкою.")


class Card(Wallet):
    def pay(self, amount: int):
        super().pay(amount)

        print(f"Ви оплатили {amount} картою.")


class Crypto(Wallet):
    def pay(self, amount: int):
        super().pay(amount)

        print(f"Ви оплатили {amount} криптовалютою.")

