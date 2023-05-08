# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# The binary number returned should be a string.

equals = []


def add_binary(a, b):
    sum = a + b
    if sum >= 1:
        add_binary(sum // 2, 0)
    equals.append(sum % 2)
    merged = ""
    for n in range(len(equals)):
        merged = merged + str(equals[n])
    merged = int(merged)
    merged = str(merged)
    if sum < 1:
        equals.clear()
    return merged


print(add_binary(1, 1))
