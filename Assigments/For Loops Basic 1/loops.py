# Basic

from audioop import mul


for i in range(0,151):
    print(i)

# Multiples of 5

for i in range(0, 1001, 5):
    print(i)

# Counting, The dojo way

for i in range(0, 101):
    if(i % 5 == 0):
        print("Coding")
    if(i % 10 == 0):
        print("Coding Dojo")

# Whoa. That sucker is huge
sum = 0
for i in range(0, 5000):
    if(i % 2 == 1):
        sum += i

# Countdown by Fours
print(sum)

for i in range(2019, 0, -4):
    print(i)

#Flexiable Counter

lownum = 2
highnum = 9
mult = 3

while(lownum <= highnum):
    if(lownum % mult == 0):
        print(lownum)
    lownum += 1
