class Car:
    def set_details(self, brand, color):
        self.brand = brand
        self.color = color

    def show_details(self):
        print(f"This Car is a {self.color} {self.brand}")


car1 = Car()
car1.set_details("Tesla", "Black")

car2 = Car()
car2.set_details("Tata", "White")

car1.show_details()
car2.show_details()