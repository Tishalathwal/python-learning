# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    def get_brand(self):
        return self.__brand  # Getter method for the private attribute
    
    def fuel_type(self):
        return "Petrol/Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric"
    
my_tesla = ElectricCar("Tesla", "Model s", "85kWh")
print(my_tesla.fuel_type())  # Demonstrating polymorphism