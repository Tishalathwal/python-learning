#  Problem: Add a static method to the Car class that returns a general description of a car.
class Car:
    car_count = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1

    def full_name(self):
        return f"{self.brand} {self.model}"

    @staticmethod
    def get_general_description():
        return "A car is a wheeled motor vehicle used for transportation."

# Example:
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
print(Car.get_general_description())  # O/p: A car is a wheeled motor vehicle used for transportation.