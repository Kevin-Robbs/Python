
class User:
    
    def __init__(self, f_name, l_name, my_color):
        self.f_name = f_name
        self.l_name = l_name
        self.my_color = my_color
    
    def greeting(self):
        print(f'Hello, my first name is {self.f_name}, my last name is {self.l_name} and my favorite color is {self.my_color}')


Player_One = User(f_name='Player', l_name='One', my_color='Royal Purple')
Player_Two = User(f_name='Player', l_name='Two', my_color='Fuschia')
Player_Three = User(f_name='Player', l_name='Three', my_color='Baby Blue, maybe!')

Player_One.greeting()
Player_Two.greeting()
Player_Three.greeting()