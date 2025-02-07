class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount, "New balance:", self.balance)
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance = self.balance - amount
            print("Withdrawn:", amount, "Remaining balance:", self.balance)
