# Exponent function using a loop
# Example: power(3, 2) → 9

def power(base, exponent):
    result = 1
    for key in range(exponent):
        result *= base
    return result

print(power(3, 4))   # 81


# Python has a built-in exponent operator (**)
print(2 ** 3)        # 8
print(5 ** 4)        # 625
print(10 ** 2)       # 100
