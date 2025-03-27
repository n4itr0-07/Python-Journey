# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# rect = Rectangle(5, 10)
# print(rect.area())


"""
Abstraction : Abstraction is the concept of hiding the real implementation of an application from the user and emphasizing only on usage of it. In python, abstraction is achieved by using abstract classes and interfaces.

Abstract Class : Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.

Abstract Method : Abstract methods are the methods that generally don’t have any implementation, it is left to the sub classes to provide implementation for the abstract methods. Abstract methods can have only method declaration but not the definition.

In python, abstraction can be achieved by using abstract classes and interfaces. Python provides a module called abc (Abstract Base Class) which provides the base for defining Abstract Base classes. Abstract base classes are classes that contain one or more abstract methods. Abstract classes can be inherited by other classes to provide the implementation of the abstract methods.

The abc module in python provides the metaclass ABCMeta which is used to define abstract base classes. The ABCMeta metaclass is used to define Abstract Base classes. The abstract base class can be inherited by other classes to provide the implementation of the abstract methods.

The abc module provides a decorator called abstractmethod which is used to define the abstract methods. The abstractmethod decorator is used to define the abstract methods in the abstract base class.

The abstract base class can be inherited by other classes to provide the implementation of the abstract methods. If the abstract methods are not implemented by the sub classes, then the sub classes will also become abstract classes.

The abstract base class can be instantiated by creating an object of the sub class. The abstract base class object cannot be created.


"""

from abc import ABC, abstractmethod

# New Example for Abstraction: Imagine you are working on a banking system. You don't want the user to know or interact directly with the underlying implementation of a bank account but only with its operations, like deposit and withdraw.

from abc import ABC, abstractmethod

# Abstract class
class BankAccount(ABC):
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    
    @abstractmethod
    def deposit(self, amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

# Concrete class implementing the abstract class
class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Invalid withdraw amount!")

# Example Usage
account = SavingsAccount("Nerdy", 5000)
account.deposit(1000)
account.withdraw(2000)
print(f"Final Balance: {account.get_balance()}")
