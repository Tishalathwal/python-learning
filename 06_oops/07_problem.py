#  Problem: Use a property decorator in the Car class to make the model attribute read-only. 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model  # Private attribute

    @property
    def model(self):
        return self.__model  # Read-only property for the model attribute
    
my_car = Car("Tata", "Safari")
print(my_car.brand)
print(my_car.model)  # Accessing the read-only property