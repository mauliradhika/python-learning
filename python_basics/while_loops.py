# Basic while loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with the loop")

print()

# Using while loop with a condition
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

print()

# While loop with break
x = 1
while x <= 10:
    if x == 5:
        break  # stops the loop
    print(x)
    x += 1
print("Loop stopped at 5")

print()

# While loop with continue
y = 0
while y < 5:
    y += 1
    if y == 3:
        continue  # skip printing 3
    print(y)