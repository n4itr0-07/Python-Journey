
#TODO: Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    # Debit Method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "Was Debated" )
        print("Current Balance is Rs.", self.balance)


    # Credit Method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "Was Credited" )
        print("Current Balance is Rs.", self.balance)

    def get_balance(self):
        return self.balance


account1 = Account(6213, 738)
# print (account1.balance)
# print (account1.account_no)
account1.debit(1000)
account1.credit(655)
account1.credit(50000)
account1.debit(15900)