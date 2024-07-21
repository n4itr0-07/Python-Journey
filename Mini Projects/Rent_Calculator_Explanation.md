# Hostel/Flat Expense Sharing Calculator

This Python script calculates the amount each person needs to pay for shared hostel/flat expenses, including rent, food, and electricity.

## Step-by-Step Explanation

1. **Input Hostel/Flat Rent:**
   ```python
   rent = int(input("Enter your hostel/flat rent :--> "))
   ```
   - The script prompts the user to input the rent for the hostel or flat.
   - `input()` function captures the user input as a string.
   - `int()` function converts the input string to an integer.

2. **Input Food Expenses:**
   ```python
   food = int(input("Enter the amount of food ordered :--> "))
   ```
   - The script prompts the user to input the total amount spent on food.
   - Similar to the rent, the input is captured as a string and then converted to an integer.

3. **Input Electricity Usage:**
   ```python
   electricity = int(input("Enter the electricity units used :--> "))
   ```
   - The script prompts the user to input the number of electricity units consumed.
   - This input is also converted from a string to an integer.

4. **Input Charge Per Unit of Electricity:**
   ```python
   charge_per_unit = int(input("Enter the charge per unit :--> "))
   ```
   - The script prompts the user to input the charge per unit of electricity.
   - The input is converted to an integer.

5. **Input Number of People Sharing the Expenses:**
   ```python
   people = int(input("Enter the number of people living in the room/flat :--> "))
   ```
   - The script prompts the user to input the number of people sharing the expenses.
   - The input is converted to an integer.

6. **Calculate Total Electricity Cost:**
   ```python
   total_amount = (electricity * charge_per_unit)
   ```
   - The script calculates the total cost of electricity by multiplying the number of units consumed (`electricity`) by the charge per unit (`charge_per_unit`).

7. **Calculate Total Amount Each Person Needs to Pay:**
   ```python
   output = (food + rent + total_amount) // people
   ```
   - The script calculates the total amount each person needs to pay.
   - The sum of food expenses (`food`), rent (`rent`), and total electricity cost (`total_amount`) is divided by the number of people (`people`).
   - `//` operator ensures the result is an integer (integer division).

8. **Print the Total Amount:**
   ```python
   print("Total amount you've to pay is :--> ", output)
   ```
   - The script prints the calculated amount each person needs to pay.

## Complete Code

```python
rent = int(input("Enter your hostel/flat rent :--> "))

food = int(input("Enter the amount of food ordered :--> "))

electricity = int(input("Enter the electricity units used :--> "))

charge_per_unit = int(input("Enter the charge per unit :--> "))

people = int(input("Enter the number of people living in the room/flat :--> "))

total_amount = (electricity * charge_per_unit)

output = (food + rent + total_amount) // people 

print("Total amount you've to pay is :--> ", output)
```