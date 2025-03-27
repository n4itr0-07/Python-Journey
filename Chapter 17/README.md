# Object-Oriented Programming (OOP) in Python

## 📌 Introduction to OOP
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, combining **data** and **methods**.

### 🎯 Key Concepts of OOP
- **Class**: Blueprint for creating objects.
- **Object**: Instance of a class.
- **Attributes**: Variables that hold data about an object.
- **Methods**: Functions defined inside a class that operate on objects.
- **Inheritance**: A class can inherit properties and methods from another class.
- **Polymorphism**: Ability to redefine methods in child classes.
- **Encapsulation**: Hiding private data and exposing only necessary parts.
- **Abstraction**: Hiding complex implementation details.

---

## 🛠️ 1. Classes and Objects

### Define a Class
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving")
```

### Create an Object
```python
my_car = Car("Toyota", "Supra")
my_car.drive()
```

### Output
```
Toyota Supra is driving
```

---

## 🛠️ 2. Constructors (`__init__` Method)
The `__init__` method is called automatically when an object is created.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 25)
print(p1.name, p1.age)
```

---

## 🛠️ 3. Inheritance
Inheritance allows a class to use methods and properties from a parent class.

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited from Animal
```

### Output
```
Animal speaks
```

---

## 🛠️ 4. Polymorphism
Polymorphism lets child classes modify methods from parent classes.

```python
class Bird:
    def sound(self):
        print("Bird chirps")

class Duck(Bird):
    def sound(self):
        print("Duck quacks")

b = Bird()
d = Duck()
b.sound()
d.sound()
```

### Output
```
Bird chirps
Duck quacks
```

---

## 🛠️ 5. Encapsulation
Encapsulation hides data using private variables (`__` prefix).

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Balance updated: {self.__balance}")

    def __secret_method(self):
        print("This is private")

acc = BankAccount(1000)
acc.deposit(500)
# acc.__balance  ❌ Error
# acc.__secret_method() ❌ Error
```

---

## 🛠️ 6. Abstraction
Abstraction hides implementation details from the user.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area())
```

---

## 🛠️ 7. Method Overloading and Overriding

### Method Overloading (Single method, different parameters)
Python doesn't support true method overloading, but we can achieve it using default values:
```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(10))
print(calc.add(10, 20))
print(calc.add(10, 20, 30))
```

### Method Overriding (Child class redefines parent method)
```python
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()
```

---

## 🛠️ 8. Getters and Setters
Control access to private variables.

```python
class Student:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

s = Student("Alex")
print(s.get_name())
s.set_name("Chris")
print(s.get_name())
```

---
