class BankAccount:

    def __init__(self, account_no, holder_name, account_type, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("\n--- Account Details ---")
        print("Account Number:", self.account_no)
        print("Account Holder:", self.holder_name)
        print("Account Type:", self.account_type)
        print("Current Balance:", self.balance)


# Getting input from user
account_no = input("Enter account number: ")
holder_name = input("Enter account holder name: ")
account_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Creating object
account1 = BankAccount(account_no, holder_name, account_type, balance)

account1.display()

# Deposit
deposit_amount = float(input("\nEnter amount to deposit: "))
account1.deposit(deposit_amount)

# Withdraw
withdraw_amount = float(input("Enter amount to withdraw: "))
account1.withdraw(withdraw_amount)

# Display updated details
account1.display()