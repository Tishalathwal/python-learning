#  Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    car_count = 0  # Class variable to keep track of the number of cars created

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1  # Increment the car count whenever a new car is created

    def full_name(self):
        return f"{self.brand} {self.model}"

# Example:
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
print(Car.car_count)  # O/p: 2