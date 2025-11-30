# Basic if statement
is_raining = True

if is_raining:
    print("Take an umbrella.")


# if-else
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# if-elif-else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# Boolean comparisons
print(10 > 5)    # True
print(10 < 5)    # False
print(10 == 10)  # True
print(10 != 5)   # True
print(7 >= 7)    # True
print(8 <= 3)    # False


# Using comparisons inside if
num = 12

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Multiple conditions (and/or)
temperature = 25

if temperature > 20 and temperature < 30:
    print("Nice weather.")

if temperature < 0 or temperature > 35:
    print("Extreme weather!")

logged_in = False
is_admin = True

if not logged_in and is_admin:
    print("Admin access denied — please log in first.")

if logged_in or not is_admin:
    print("Either logged in OR not an admin — some access allowed.")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(10, 7, 12))