class Car:
    # __brand = None
    # __models = None
    def __init__(self, brand, models):
        self.__brand = brand
        self.models = models

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.models}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    

class ElectricCar(Car):
    def __init__(self, __brand, models, battery_capacity):
        super().__init__(__brand, models)
        self.battery_capacity = battery_capacity

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("tesla", "models S", "85kwh")

# print(my_tesla.full_name())



my_car = Car("Toyota", "Lamborghini")
# print(my_car.__brand)
# print(my_car.models)

# print(my_car.full_name())

# print(my_tesla.full_name())
print(my_tesla.fuel_type())