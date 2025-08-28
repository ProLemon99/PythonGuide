# A class is a blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects will have.

# Example of a class
class Car:
    def __init__(self, brand, color): # The attributes
        self.brand = brand
        self.color = color

    def drive(self): # The method
        print(f"{self.color} {self.brand} is driving!")

# Create an object (instance) of Car
my_car = Car("Toyota", "Red")
my_car.drive()

# Key points:

# __init__ is a constructor; it initializes object properties.
# Objects are instances of a class.