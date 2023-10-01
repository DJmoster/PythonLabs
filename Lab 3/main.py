from models.enums import *
from models.client_types import Client, Critic
from models.payment_methods import Crypto, Cash
from models.restaurants import SushiRestaurant, PizzaRestaurant, SteakhouseRestaurant

sushi_restaurant = SushiRestaurant()
pizza_restaurant = PizzaRestaurant()
steak_restaurant = SteakhouseRestaurant()

client = Client("John", Crypto(10_000))
critic = Critic("Alex", Cash(1_000), 0.5)

sushi_restaurant.visit(client)

sushi_restaurant.order(client, SushiMenu.PHILADELPHIA)
sushi_restaurant.order(client, SushiMenu.CHICKEN_BOWL)
sushi_restaurant.leave(client)

print(f"\nБаланс ресторану: {sushi_restaurant.balance}")
print(f"Рейтинг ресторану: {sushi_restaurant.rating}")
print(f"Баланс клієнта: {client.wallet.balance}")
print()

pizza_restaurant.visit(critic)
pizza_restaurant.order(critic, PizzaMenu.PIZZA_HAWAIIAN)
pizza_restaurant.leave(critic)

pizza_restaurant.rate(critic, 100)

print(f"\nБаланс ресторану: {pizza_restaurant.balance}")
print(f"Рейтинг ресторану: {pizza_restaurant.rating}")
print(f"Баланс клієнта: {critic.wallet.balance}")