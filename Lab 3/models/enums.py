from enum import Enum


class SushiMenu(Enum):
    PHILADELPHIA = ("Філадельфія", 500)
    CHICKEN_BOWL = ("Боул з куркою", 300)


class PizzaMenu(Enum):
    PIZZA_4_CHEESES = ("Піца 4 сири", 1000)
    PIZZA_HAWAIIAN = ("Гавайська піца", 800)


class SteakhouseMenu(Enum):
    STEAK_RIBEYE = ("Стейк Рібай", 1500)
    STEAK_NEW_YORK = ("Стейк Нью-Йорк", 2000)

