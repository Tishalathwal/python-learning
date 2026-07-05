#  Problem:  Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    def __init__(self, batterySize):
        self.batterySize = batterySize  

class Engine:
    def __init__(self, engineType):
        self.engineType = engineType

class ElectricCar(Battery, Engine):
    def __init__(self, brand, model, batterySize, engineType):
        Battery.__init__(self, batterySize)
        Engine.__init__(self, engineType)
        self.brand = brand
        self.model = model

my_tesla = ElectricCar("Tesla", "Model S", "100kWh", "Electric")
print(my_tesla.brand)        # O/p: Tesla
print(my_tesla.model)        # O/p: Model S
print(my_tesla.batterySize)  # O/p: 100kWh
print(my_tesla.engineType)   # O/p: Electric