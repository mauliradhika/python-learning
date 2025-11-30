# 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Accessing elements
print(number_grid[0][0])   
print(number_grid[1][2])   

# Nested loops
for row in number_grid:
    for item in row:
        print(item)

# Matrix-style print
for row in number_grid:
    print(row)

# Sum of all values
total = 0
for row in number_grid:
    for item in row:
        total += item

print("Total:", total)