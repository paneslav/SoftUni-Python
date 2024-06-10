from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, liters):
        pass


class Car(Vehicle):
    SUMMER_MULTIPLIER = 0.9

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + Car.SUMMER_MULTIPLIER) * distance
        if fuel_needed > self.fuel_quantity:
            return

        self.fuel_quantity -= fuel_needed

    def refuel(self, liters):
        self.fuel_quantity += liters


class Truck(Vehicle):
    SUMMER_MULTIPLIER = 1.6

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + Truck.SUMMER_MULTIPLIER) * distance
        if fuel_needed > self.fuel_quantity:
            return

        self.fuel_quantity -= fuel_needed

    def refuel(self, liters):
        self.fuel_quantity += (liters * 0.95)


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)