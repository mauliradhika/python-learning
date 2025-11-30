# Tuples are like lists but IMMUTABLE (cannot be changed)

coordinates = (4, 5)
print(coordinates)
print(coordinates[0])      # 4
print(coordinates[1])      # 5

# List of tuples
points = [(1, 2), (3, 4), (5, 6)]
print(points)

# Length and membership
print(len(coordinates))    # number of elements
print(4 in coordinates)    # True
print(7 in coordinates)    # False

# Tuple with different data types
person = ("Priyanka", 20, "India")
print(person)

# Tuple unpacking = assigning each element of a tuple to separate variables
x, y = coordinates
print(x, y)