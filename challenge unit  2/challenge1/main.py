class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited Rs.{amount} into Account {self.__account_number} ({self.__account_holder_name}).")
        else:
            print("Invalid deposit amount. Amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew Rs.{amount} from Account {self.__account_number} ({self.__account_holder_name}).")
        elif amount <= 0:
            print("Invalid withdrawal amount. Amount should be greater than 0.")
        else:
            print("Insufficient balance for withdrawal.")

    def display_balance(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder Name: {self.__account_holder_name}")
        print(f"Account Balance: Rs.{self.__account_balance}")

# Create an instance of the BankAccount class
account1 = BankAccount("212203767", "NITHISHKUMAR A S")

# Deposit and withdraw money
account1.display_balance()
account1.deposit(100000)
account1.withdraw(54500)
account1.display_balance()
