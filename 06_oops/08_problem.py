#  Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

my_tesla = ElectricCar("Tesla", "Model S", "100kWh")

print(isinstance(my_tesla, Car))        # O/p: True
print(isinstance(my_tesla, ElectricCar))  # O/p: True