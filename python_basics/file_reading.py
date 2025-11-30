# Reading a file
textfile = open("test.txt", "r")   # open file in read mode

print(textfile.readable())         # check if file is readable
print(textfile.read())             # read entire file
print(textfile.readline())         # read first line
print(textfile.readline())         # read second line
print(textfile.readlines())        # read remaining lines as list

textfile.close()                   # close the file


# Read line by line
with open("test.txt", "r") as file:   # auto-closes file
    print("\nRead line by line:")
    print(file.readline())            # first line
    print(file.readline())            # second line


# Loop through lines
with open("test.txt", "r") as file:
    print("\nLooping through lines:")
    for line in file:                 # iterate through each line
        print(line)                   # print each line


# Read into list
with open("test.txt", "r") as file:
    lines = file.readlines()          # entire file as list of lines
    print("\nList of lines:", lines)


# Writing ("w" mode)
with open("test.txt", "w") as file:   # overwrites the file
    file.write("Line 1\n")            # write line 1
    file.write("Line 2\n")            # write line 2


# Appending ("a" mode)
with open("test.txt", "a") as file:   # adds to the end of file
    file.write("Appended line\n")     # write appended line


# Final read
with open("test.txt", "r") as file:   # read file again
    print("\nFinal content:")
    print(file.read())                # print full file