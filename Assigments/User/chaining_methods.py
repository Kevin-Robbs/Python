class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        print(f'Your deposit of {amount} dollars is being processed...\n')
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        print(f'Your withdrawal of {amount} dollars is being processed...\n')
        self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f'Your balance is now {self.balance} dollars\n')
        return self

    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        print(f'Your monthly interest statement is here!')
        print('_________________________________________________\n')
        print(f'With your current rate of {self.int_rate * 100}%:')
        return self
        

account_one = BankAccount(.02, 2000)
account_two = BankAccount(.04, 5000)

account_one.deposit(500).deposit(825).deposit(100).withdraw(900).yield_interest().display_account_info()
account_two.deposit(100).deposit(925).yield_interest().display_account_info()