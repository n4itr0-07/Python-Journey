# Understanding Statically Typed vs. Dynamically Typed Variables

## Statically Typed Variables

In statically typed languages, the type of each variable is **explicitly declared and determined at compile time**. Once a variable’s type is set, it cannot change. This characteristic is enforced by the compiler, and trying to assign a value of a different type will result in a compilation error.

### Key Characteristics of Statically Typed Variables
1. **Type Declaration**: You must explicitly declare the type of a variable when you define it.
2. **Type Checking at Compile Time**: The compiler verifies type correctness before the program runs, preventing certain types of errors early.
3. **Type Consistency**: Once assigned, a variable must always store values of the declared type.

### Example in Java (a statically typed language):
```java
int age = 25;     // Declaring an integer
age = "twenty";   // Compilation error! Can't assign a string to an integer
```

Here, the `age` variable is declared as an integer, and the compiler ensures it holds only integer values throughout the program.

### Example in C++ (another statically typed language):
```cpp
int count = 10;
double price = 99.99;
count = "hello";  // Error! Trying to assign a string to an integer
```

In statically typed languages like C++, Java, C#, and Swift, types are strictly enforced, helping catch many bugs at compile time.

---

## How Does This Differ from Python?

Python is a **dynamically typed language**, meaning variable types are determined at runtime. You don’t need to declare the type explicitly; instead, Python infers the type based on the value assigned. Moreover, a variable’s type can change throughout the program.

### Key Characteristics of Python's Dynamic Typing
1. **No Type Declarations**: Variable types are not declared in Python; they’re inferred from the assigned value.
2. **Type Checking at Runtime**: Type checking occurs when the program runs, not at compilation.
3. **Type Flexibility**: Variables can hold values of different types at different points.

### Example in Python:
```python
age = 25      # Initially an integer
age = "twenty"  # Now 'age' is a string. No error occurs.
```

In this example, the `age` variable initially holds an integer, then a string. Python’s dynamic typing allows this flexibility, but errors related to types will only be caught at runtime.

### Another Example in Python:
```python
price = 99.99   # price is a float
price = "expensive"  # price is now a string
```

Python changes the `price` variable type without any error, demonstrating dynamic typing's flexibility.

---

## Major Differences Between Statically Typed and Dynamically Typed Variables

| Feature            | Statically Typed Languages               | Dynamically Typed Languages (e.g., Python)  |
|--------------------|------------------------------------------|---------------------------------------------|
| **Type Declaration** | Must be declared explicitly            | Not required                                |
| **Type Checking**  | Done at compile time                     | Done at runtime                             |
| **Type Safety**    | Errors caught before runtime             | Errors caught during execution              |
| **Type Flexibility** | Variables maintain a single type       | Variables can change types                  |
| **Performance**    | Generally faster (types known at compile time) | Slower (type checks at runtime)           |
| **Code Example**   | `int age = 25;`                          | `age = 25`                                  |
| **Errors**         | Caught at compile time                   | Occur at runtime                            |

---

## Benefits and Drawbacks of Both Approaches

### Statically Typed Variables
**Advantages**:
- **Early error detection**: Type errors are caught at compile time, which can prevent certain bugs early.
- **Performance**: Statically typed languages are often faster because types are known at compile time.
- **Predictability**: The variable's type is constant, making debugging easier.

**Disadvantages**:
- **Less flexibility**: The programmer must specify types, making the code more rigid.
- **More code**: Extra code for type declarations can make development slower and more verbose.

### Dynamically Typed Variables (as in Python)
**Advantages**:
- **Flexibility**: Variables can hold different types of data, simplifying code and facilitating rapid changes.
- **Faster development**: Type declarations aren’t needed, speeding up development.

**Disadvantages**:
- **Potential runtime errors**: Type errors occur at runtime, which may be harder to trace.
- **Performance overhead**: Type checks at runtime can slow down execution.

---

## Type Hinting in Python (Optional Static Typing)

To bridge the gap, Python introduced **type hinting** (since Python 3.5). Type hinting allows specifying expected types without enforcing them, combining dynamic flexibility with improved readability and error detection.

### Example of Type Hinting in Python:
```python
def atm_withdrawal(balance: float, amount: float) -> float:
    if amount > balance:
        return balance
    return balance - amount
```

In this example:
- `balance: float` and `amount: float` indicate expected float values.
- `-> float` specifies that the function should return a float.

While not enforced, type hints improve readability and enable tools like linters or type checkers (e.g., `mypy`) to detect type mismatches before runtime.

---

## Conclusion
- **Statically Typed Variables**: In languages like Java or C++, types are declared and checked at compile time, providing safety and performance benefits.
- **Dynamically Typed Variables**: Python determines types at runtime, offering flexibility but potentially leading to runtime errors.
- **Type Hinting in Python**: Allows documenting expected types, improving readability and error checking without strict enforcement.
