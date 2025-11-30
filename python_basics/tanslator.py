# Translator: Replace vowels with 'g' or 'G'

def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in "aeiou":      # check if vowel
            if letter.isupper():
                result += "G"
            else:
                result += "g"
        else:
            result += letter
    return result

print(translate("Shivi is learning Python"))
print(translate("HELLO"))
