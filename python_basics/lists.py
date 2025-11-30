friends = ["Kevin" , "Karen" , "Jim" , "Oscar" , "Toby"]
print(friends)

print(friends[1])        # Karen
print(friends[-2])       # Oscar (negative index counts from end)
print(friends[1:3])      # ['Karen', 'Jim']
print(friends[1:])       # ['Karen', 'Jim', 'Oscar', 'Toby']

# List Functions

lucky_numbers = [4, 8, 15, 15, 15, 16, 23, 42]
friends.extend(lucky_numbers)  # adds all elements of lucky_numbers to the friends list
print(friends)

friends.append("Creed")        # adds element at the end
friends.insert(1, "Kelly")     # inserts at index 1

friends.remove("Jim")          # removes the first occurrence of "Jim"
friends.pop()                  # removes the last element

friends.clear()                # removes all elements from the list

lucky_numbers.sort()        # sorts the list in ascending order
print(lucky_numbers)

lucky_numbers.reverse()     # reverses the list order
print(lucky_numbers)

print(lucky_numbers.index(23))   # returns the index of first occurrence of 23
print(lucky_numbers.count(15))   # returns how many times 15 appears

lucky_copy = lucky_numbers.copy()  # creates a copy of the list
print(lucky_copy)