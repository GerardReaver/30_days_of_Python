# This is the code for Day 3 of the 30 day Python challenge. 
# we are learning about boolean operators. True or False values and how to use them in Python.
print(True)
print(False)

# Operators.
# Arithmetic Operators include +, -, *, /, %, **, //.
print("Addition: ", 1 + 1)
print("Subtraction: ", 2 - 1)
print("Multiplication: ", 2 * 3)
print("Division: ", 4 / 2)
print("Division with remainder: ", 5 / 2) # This will give us a float value
print("Division without remainder: ", 5 // 2) # This will give us an integer value
print("Modulus: ", 5 % 2) # This will give us a value with a remainder
print("Exponental: ", 2 ** 3) 

# Combining boolean operators and arithmetic operators. 
print(3 > 2 and 4 < 5) # This will print True
print(3 > 4 or 4 < 5) # This will print True because only one had to be true
print(3 > 4 or 4 > 5) # This will print False because both are false

# Here are some more comparison operators
# Is: returns True if both variables are the same object.
x = 2
y = 2
print("x is y", x is y)
# Is not: returns True if both variables are not the same object.
z = 3
print("x is not z", x is not z)
# in: returns True if a sequence with the specified value is present in the object.
list1 = [1, 2, 3, 4, 5]
print(f"This is list one", list1)
print("1 is in list1", 1 in list1)
print("6 is in list1", 6 in list1)
# not in: returns True if a sequence with the specified value is not present in the object.
print("6 is not in list1", 6 not in list1)

# Time to do the problems for day 3. 

# Declare your age as an integer, height as a float, and a variable that stores a complex number. 
# #1, #2, #3 complete
age = 32
height = 5.5
compplex_num = 2 + 3j
# Write a scipt that prompts the user to enter base and height of a triangle and calculate the area of the triangle (area = 0.5 * base * height).
# #4 complete
base = float(input("Enter base : "))
height = float(input("ENter height: "))
area = 0.5 * base * height
# Write a scipt that prompts the user to enter the three sides of a triangle and calculate the perimeter of the triangle (perimeter = side1 + side2 + side3).
# #5 complete
print("Area of triangle is: ", area)
triangle_side1 = int(input("Enter Side 1: "))
triangle_side2 = int(input("Enter Side 2: "))
triangle_side3 = int(input("Enter Side 3: "))
triangle_perimeter = triangle_side1 + triangle_side2 + triangle_side3
print("Perimeter of triangle is: ", triangle_perimeter)
# Write a scipt to get the area and perimeter of a rectangle using the length and width.
# #6 complete
length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print("Area of a rectangle is: ", rectangle_area)
print("Perimeter of a rectangle is: ", rectangle_perimeter)
# Write a scipt to get the area and circumference of a circle using the radius.
# #7 complete
pi = 3.14
radius = int(input("Enter radius of circle: "))
circle_area = pi * (radius * radius) 
# Some mathematical problems are skipped as i have no interst in solving slopes in my field of work. 
# Find the length of "Python" and "dragon" and make a falsy comparison statement.
# #8 complete
python_length = len("Python")
dragon_length = len("Dragon")
print(python_length is not dragon_length)
# Find the length of "Python" and "dragon" and make a truthy comparison statement.
# #9 complete
python = "Python"
dragon = "Dragon"
print("on" in "python" and "on" in "Dragon")
# Find the length of the text "python" and convert the value to a float and convert it to a string.
python_length = len("python")
print(python_length)
python_length = float(python_length)
print(python_length)
python_length = str(python_length)
print(python_length)
# Check to see if a number is even in python. 
# # #10 complete
given_number = int(input("Enter a number: "))
number_even_check = given_number % 2 == 0
print(f"Is the number even? {number_even_check}")
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# #11 complete
result1 = 7 // 3
print(result1)
result2 = 2.7
result2 = int(result2)
print(result2)
print(result1 == result2)
# Check if the type of '10' is equal to 10.
# #12 complete
print(type("10"))
print(type(10))
print(type("10") == type(10))
# Check if int('9.8') is equal to 10.
# #13 complete
print(int(9.8) == 10)
