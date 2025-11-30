# Basic for loop
for letter in "Python":
    print(letter)


# Looping through a list
friends = ["Kevin", "Karen", "Jim"]
for friend in friends:
    print(friend)


# Looping with range()
for num in range(5):
    print(num)   # 0 to 4


# Range with start and end
for num in range(2, 6):
    print(num)   # 2, 3, 4, 5


# Looping through indices
for index in range(len(friends)):
    print(friends[index])


# Using for loop with if
for num in range(1, 6):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
