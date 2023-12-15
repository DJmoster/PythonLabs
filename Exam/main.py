from service import *
from factory import CarRentalServiceFactory

client1 = Client('Sviat', 10000)
client2 = Client('Jonh', 1000)

service = CarRentalService(
    cars=[
        Car(2001, 'Toyota', 150, 3000),
        Car(2020, 'Mercedes Benz', 300, 10000),
        Car(2012, 'Opel', 100, 1000),
    ]
)

service2 = CarRentalServiceFactory.create()
print(service2.rent(client1, service2.cars[0], 2))
print(client1.money)

rent = service.rent(client1, service.cars[0], 10)
print(service.rent(client1, service.cars[1], 11))

rent = service.continue_rent(rent, 10)
print(rent)


print(service.available_cars)
print(service.my_rents(client1))

print(client1.money)

