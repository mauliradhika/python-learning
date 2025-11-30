# Basic function with parameter
def sayHi(name):
    print(f"Hello {name}")

sayHi("Shivi")
sayHi("Steve")


# Function that returns a value
def square(num):
    return num * num   # returns the result

print(square(5))       # 25


# Function with multiple parameters
def add(a, b):
    return a + b

print(add(3, 4))       # 7


# Function with default parameters
def greet(name="User"):
    print(f"Welcome, {name}!")

greet() # Welcome, User!
greet("Priyanka") # Welcome, Priyanka!


# Function returning multiple values (tuple unpacking)
def get_info():
    return "Priyanka", 20

name, age = get_info()
print(name, age)


# Function with logic + return
def is_even(num):
    return num % 2 == 0

print(is_even(10))     # True
print(is_even(7))      # False