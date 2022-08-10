num1 = 42 #variable declaration, primitive type Number

num2 = 2.3 #variable declaration, primitive type Number, type float(decimal)

boolean = True #variable declaration, primitive type Boolean

string = 'Hello World' #variable declaration, primitive type String

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List declaration with values 

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Dictionary Declaration

fruit = ('blueberry', 'strawberry', 'banana') #Tuple declaration

print(type(fruit)) #type check

print(pizza_toppings[1]) #list access value

pizza_toppings.append('Mushrooms') #list add value

print(person['name']) #dictionary access value

person['name'] = 'George' #dictionary change value

person['eye_color'] = 'blue' #dictionary add value

print(fruit[2]) #access tuple value

if num1 > 45: #if conditional
    print("It's greater")
else: # else conditional
    print("It's lower")

if len(string) < 5: #if conditional
    print("It's a short word!")
elif len(string) > 15: #else if conditional
    print("It's a long word!")
else: #else conditional
    print("Just right!")

for x in range(5): #for loop
    print(x)
for x in range(2,5): #for loop
    print(x)
for x in range(2,10,3):
    print(x)

x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break



def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()



def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)



def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)