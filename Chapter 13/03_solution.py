class Car:
    # brand = None
    # model = None
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity


my_tesla = ElectricCar("tesla", "Model S", "85kwh")

print(my_tesla.full_name())



my_car = Car("Toyota", "Lamborghini")
print(my_car.brand)
print(my_car.model)

print(my_car.full_name())

print(my_tesla.full_name())