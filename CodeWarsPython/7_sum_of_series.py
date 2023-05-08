# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

"""
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""


def get_sum(a, b):
    sum = 0
    if a == b:
        return a
    elif a < b:
        while a <= b:
            sum = sum + a
            a = a + 1
        return sum
    elif b < a:
        while b <= a:
            sum = sum + b
            b = b + 1
        return sum


print(get_sum(0, -1))
