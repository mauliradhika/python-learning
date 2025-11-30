# Basic try-except
try:
    number = int(input("Enter a number: "))
    print(number)
except: #except ValueError
    print("Invalid input")


# Handling specific errors
try:
    value = 10 / 0
except ZeroDivisionError as err:
    print(err)


# Multiple except blocks
try:
    num = int("abc")
except ValueError:
    print("ValueError: That was not a number.")
except:
    print("Some other error occurred.")


# Try-except with else
try:
    age = int(input("Enter your age: "))
except:
    print("Invalid age")
else:
    print("You entered:", age)


# Try-except with finally
try:
    print("Inside try block")
finally:
    print("This always runs (finally block)")
