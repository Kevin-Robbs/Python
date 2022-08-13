class User:
    def __init__(self, first_name, last_name, email, age):
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def __repr__(self):

       return f'User info: \nFirst Name: {self.fname} \nLast Name: {self.lname} \nEmail: {self.email} \nAge: {self.age}'
    
    def display_info(self):

        print(f'User info \nFirst Name: {self.fname} \nLast Name: {self.lname} \nEmail: {self.email} \nAge: {self.age}\n')
        return self

    def enroll(self):
        if self.is_rewards_member == False:
            print(f'{self.fname}, you have enrolled in our rewards program')
            self.gold_card_points = 200
            print(f'Your total rewards points are {self.gold_card_points}!\n')
            self.is_rewards_member = True
        else:
            print('Looks like you already signed up to be a rewards member')
            print(f'You have {self.gold_card_points} points remaining\n')
        return self

    def spend_points(self, amount):

     total_points = self.gold_card_points - amount

     if total_points < 0:
        print('Insufficient points on your account, please try again!')
        print(f'You only have {self.gold_card_points} points to spend\n')
     else:
        print(f'You have {self.gold_card_points} points to spend')
        print(f'You are spending {amount} points...')
        print(f'You have {total_points} points left\n')
        self.gold_card_points = total_points
        return self

user_one = User('Kevin', 'Robbs', 'kevin@myemail.com', 32)
user_two = User('Molly', 'Robbs', 'molly@myemail.com', 24)
user_three = User('Birdie', 'Robbs', 'birdie@myemail.com', 1)

user_one.display_info().enroll().spend_points(50).enroll()
user_two.display_info().enroll()
user_three.display_info().enroll().spend_points(201)