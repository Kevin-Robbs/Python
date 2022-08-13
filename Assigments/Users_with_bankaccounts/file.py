class BankAccount:
    
    num_of_accounts = []

    def __init__(self, int_rate, balance): 
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.num_of_accounts.append(self)

    def deposit(self, amount):
        print(f'Your deposit of {amount} dollars is being processed...\n')
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Please try again")
        else:
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
        

class User:

    def __init__(self, name="N/A", email=''):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        self.account.display_account_info()
        return self

user_one = User('Kevin', 'kevin@dojo.com')
user_one.make_deposit(1000).make_deposit(2000).make_withdrawl(300).display_user_balance()
user_two = User('Molly', 'molly@dojo.com')
user_two.make_deposit(500).make_deposit(1000).make_withdrawl(900).display_user_balance()