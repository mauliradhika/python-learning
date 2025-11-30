print("Mauli \nRadhika") #next line
print("Mauli \" Radhika")  # \ escape character renders the next char


phrase = "This is a variable"

print(phrase + " which can be concatenated")  # string concatenation
print(phrase.lower())        # converts to lower case
print(phrase.upper())        # converts to upper case
print(phrase.isupper())      # checks if the string is entirely uppercase
print(phrase.upper().isupper()) # function chaining (upper -> isupper)
print(len(phrase))           # length of the string
print(phrase[1])             # character at index 1 (0-based indexing)
print(phrase.index("a"))     # index of first 'a'
print(phrase.index("iab"))  # starting index of substring "conc"
print(phrase.replace("This", "Here"))  # replaces first substring with second substring
print(phrase.find("is"))  # returns starting index OR -1 if not found
print("   hello   ".strip())  # removes leading and trailing spaces
print("   hello".lstrip())  # remove left spaces
print("hello   ".rstrip())  # remove right spaces
print(phrase.split())  # splits on spaces → ['This', 'is', 'a', 'variable']
words = ["Mauli", "Radhika"]
print(" ".join(words))  # join list with spaces
print(phrase.startswith("This"))  # True
print(phrase.endswith("variable"))  # True
print(phrase.count("i"))  # how many times 'i' appears
print(phrase.title())  # "This Is A Variable", capitalizes each word
print(phrase.swapcase())  # "tHIS IS A VARIABLE"
print("abc".isalpha())  # True (only letters)
print("123".isdigit())  # True (only digits)
print("abc123".isalnum())  # True (letters + digits)
print("HelloWorld".removeprefix("Hello"))  # "World"
print("HelloWorld".removesuffix("World"))  # "Hello"
print("aaa".replace("a", "b", 2))  # replace only first 2 occurrences