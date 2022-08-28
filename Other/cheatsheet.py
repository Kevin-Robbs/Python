
# # # # # x = 1

# # # # # print('my favorite number is', type(x)) #this will print out the correct result
# # # # # print('my favorite number is ' + str(1)) #this will print out an error

# # # # # my favorite number is <class 'int'>
# # # # # my favorite number is 1

# # # # animals = ["dog", "cat", "lizard", "mouse", "rhino", "bear"]

# # # # animals.sort()

# # # # print(animals)

# # # # def add(a,b):
# # # #     x = a + b
# # # #     print(x)

# # # # def myFunction(name='Player', age = 0):
# # # #     print(f"Hello, my name is {name} and I am {age} years old!")

# # # # myFunction(32, 'Kevin')

# # # #switch statement
# # # def powerRanger(number):
# # #     switch={
# # #         1: 'Red Ranger',
# # #         2: 'Blue Ranger',
# # #         3: 'Yellow Ranger',
# # #         4: 'Pink Ranger',
# # #         5: 'Black Ranger',
# # #         6: 'Green Ranger',
# # #         7: 'White Ranger'
# # #     }

# # #     return switch.get(number, 'Power Ranger does not exist, Try again!')

# # # print(powerRanger(7))

# # class powerRanger:
# #     def __init__(self, color, weapon):
# #         self.color = color.capitalize()
# #         self.weapon = weapon.capitalize()

# #     def phrase(self):
# #         print(f'The {self.color} Ranger is equipped with a {self.weapon}')

# # redRanger = powerRanger('red', 'sword')
# # blueRanger = powerRanger('Blue', 'dagger')
# # yellowRanger = powerRanger('yellow', 'pistol')

# # redRanger.phrase()
# # blueRanger.phrase()
# # yellowRanger.phrase()

# class BankAccount:
#     bankName = "Federal Bank of Banks"
#     all_accounts = []

#     def __init__(self, type, total, name):
#         self.total = total
#         self.type = type
#         self.name = name
#         BankAccount.all_accounts.append({'Type': self.type, 'Total': self.total, 'Name': self.name})

#     def __repr__(self):
#         return f'Total: {self.total}, Type: {self.type}'

#     def greeting(self):
#         print(f'Hello {self.name}, your {self.type} account has {self.total} dollars in it!')

#     @classmethod
#     def changeBankName(cls, name):
#         cls.bankName = name
#         print(f'The new bank name is {cls.bankName}')

#     @classmethod
#     def all_totals(cls):
#         sum = 0
#         for i in cls.all_accounts:
#             sum += i['Total']
#         print(sum) 

# account1 = BankAccount('Checking', 1000000, 'Molly')
# account2 = BankAccount('Checking', 6000, 'Kevin')
# account3 = BankAccount('Checking', 32000, 'Birdie')
# # account4 = BankAccount('Checking', 34500)

# BankAccount.all_totals()

