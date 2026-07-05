# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

class Car():
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model

    def get_brand(self):
        return self.__brand  # Getter method for the private attribute
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize



my_tesla = ElectricCar("Tesla", "Model s", "85kWh")
print(my_tesla.get_brand())  # Accessing the private attribute using the getter method
