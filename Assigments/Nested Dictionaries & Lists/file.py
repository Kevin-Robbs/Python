# Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]

x[1][0] = 15
print(x[1][0])
########################################

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name'] = 'Bryant'
print(students[0]['last_name'])
########################################

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'][0])
########################################

z = [ {'x': 10, 'y': 20} ]

z[0]['y'] = 30
print(z[0]['y'])


# Iterate through a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for entry in list:
        print(f"first_name - {entry['first_name']}, last_name - {entry['last_name']} ")

iterateDictionary(students)


#Get Values from a list of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for entry in some_list:
        print(entry[key_name])

iterateDictionary2('last_name', students)

#Iterate through a dictionary with list values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(myDict):
    loc_length = len(myDict['locations'])
    inst_length = len(myDict['instructors'])

    print(f"{loc_length} LOCATIONS")
    for val in myDict['locations']:
        print(val)
    print(' ')
    print(f"{inst_length} LOCATIONS")
    for val in myDict['instructors']:
        print(val)

printInfo(dojo)
