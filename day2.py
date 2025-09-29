# Day 2: 30 Days of Python programming
# TODAY WE START VARIABLES IN PYTHON
print('Hello, World!') # This text is an argument
print('Hello', ',', 'World', '!') # This text has 4 arguments
print(len('Hello, World!')) # This text has 1 argument

# This was a good way to explain fully the uses of the print function and how those arguments work. 
# Now we will start with variables
first_name = 'Gerard' 
last_name = 'Ben'
country = 'USA'
city = 'New York'
age = 31
is_married = False
skills = ['MySQL', 'Python', 'Java']
person_info = {
    'first_name': 'Gerard',
    'last_name': 'Ben',
    'country': 'USA',
    'city': 'New York'
    }

# This was a good way to explain and list some variables from strings, intergers, booleans, lists, and dictionaries.
# Now we will printg the values stored in the variables. 

print('First name;', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

 # multiple variables can also be declared in one line

first_name, last_name, country, age, is_married = 'Gerard', 'Ben', 'USA', 31, False
# That was just a way to show how to declare multiple variables in the same line. 
print(first_name, last_name, country, age, is_married)

# Now i will demonstrate how to get user input
first_name = input('What is your name: ')
age = input('How old are you: ')


# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Gerard'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Gerard'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Gerard'
print(first_name)               # 'Gerard'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['G', 'e', 'r', 'a', 'r', 'd']

# The Exercises for Day 2
# Day 2 of 30 Days of Python Programming
first_name = 'Gerard'
last_name = 'Ben'
full_name = first_name + ' ' + last_name
country = 'USA'
city = 'New York'
age = 31
year = 2025
is_married = False
is_true = True
is_light_on = True
var1, var2, var3 = 1, 2, 3

# Excercises level 2
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year)
type(is_married)
type(is_true)
type(is_light_on)
type(var1)
type(var2)
type(var3)

len(first_name)
len(last_name)
num_one = 5
num_two = 4
variable_total = num_one + num_two
variable_diff = num_one - num_two
variable_product = num_one * num_two
variable_division = num_one / num_two 
variable_remainder = num_one % num_two 
variable_exp = num_one ** num_two
variable_floor_div = num_one // num_two 

# Time for some harder math problems
# the circumference of a circle = 2πr
radius = 30
pi = 3.14
circumference_of_circle = 2 * pi * radius
area_of_circle = pi * radius ** 2 

# CONGRATULATIONS YOU HAVE COMPLETED DAY 2 OF 30 DAYS OF PYTHON PROGRAMMING