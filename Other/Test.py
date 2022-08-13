class User:
    def __init__(self, f_name, l_name, age, gender, is_employee, is_manager):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender
        self.is_employee = is_employee
        self.is_manager = is_manager

    def greeting(self):
        print(f"Hello and Welcome {self.f_name} {self.l_name}")

user_kevin = User('Kevin', 'Robbs', 32, 'Male', False, True)

user_kevin.greeting()