# Base Class
class Animal:
    def move(self):
        pass

# Dog Class
class Dog(Animal):
    def move(self):
        print("The dog is running 🐕")

# Bird Class
class Bird(Animal):
    def move(self):
        print("The bird is flying 🦅")

# Base Class for Vehicles
class Vehicle:
    def move(self):
        pass

# Car Class
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗")

# Plane Class
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️")

# Testing Polymorphism

# Animal Objects
dog = Dog()
bird = Bird()

# Vehicle Objects
car = Car()
plane = Plane()

# Calling move() on each object
animals = [dog, bird]
vehicles = [car, plane]

# Loop through and call move for all animal objects
print("Animal Movement:")
for animal in animals:
    animal.move()

# Loop through and call move for all vehicle objects
print("\nVehicle Movement:")
for vehicle in vehicles:
    vehicle.move()
