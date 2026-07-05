#  Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize= batterySize

my_tesla = ElectricCar("Tesla", "Model s", "85kWh")
print(my_tesla.batterySize)
