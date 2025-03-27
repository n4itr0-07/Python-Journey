class bankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private Variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Balance updated: {self.__balance}")

    def __secret_method(self):
        print("This is private")

acc = bankAccount(1000)
acc.deposit(100)