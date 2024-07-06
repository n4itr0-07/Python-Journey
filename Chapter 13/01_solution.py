class Car:
    # brand = None
    # model = None
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Lamborghini")
print(my_car.brand)
print(my_car.model)

