class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private variable
        self.__balance = balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("You do not have that much balance in your account !!")
        
    def get_balance(self):
        return self.__balance  # public method for accessing private variable


abhi = BankAccount(101,999999)
print(abhi.get_balance())
abhi.deposit(1)
print(abhi.get_balance())
abhi.withdraw(11111)

