#1 Countdown
def countdown(number):
    list = []

    for i in range(number, -1, -1):
        list.append(i)

    return list

print(countdown(91))


#2 Print and Return
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([4,5]))

#3 First Plus Length
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

print(first_plus_length([1,2,5,7,5,8]))

#4 Values Greater than Second

def values_greater_than_second(list):

    if(len(list) < 2):
        print(False)
    else:
        new_list = []
        for i in range(0, len(list)):
            if(list[i] > list[1]):
                new_list.append(list[i])
        
        print(f"There are {len(new_list)} values that are greater than {list[1]}")
        print("You can view those here:")
        print(new_list)

values_greater_than_second([2])

#5 This Length, That Value

def length_and_value(size, value):
    list = []

    for i in range(size):
        i = value
        list.append(i)

    print(list)

length_and_value(3,7)

user_age = input("Enter your age:")

print(f"You are {user_age} years old")