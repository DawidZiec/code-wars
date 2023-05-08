'''
You are given an array (which will have a length of at least 3, but could be very large)
containing integers. The array is either entirely comprised of odd integers or entirely
comprised of even integers except for a single integer N. Write a method that takes the
array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''


def odd_or_even(integers):
    if integers[0] % 2 == 0:
        if integers[1] % 2 == 0:
            return 'even'
        else:
            if integers[2] % 2 == 0:
                return 'even'
            else:
                return 'odd'
    else:
        if integers[1] % 2 == 1:
            return 'odd'
        else:
            if integers[2] % 2 == 1:
                return 'odd'
            else:
                return 'even'


def find_outlier(integers):
    number = []
    if odd_or_even(integers) == 'odd':
        while len(number) == 0:
            for integer in integers:
                if integer % 2 == 0:
                    number.append(integer)
    else:
        while len(number) == 0:
            for integer in integers:
                if integer % 2 == 1:
                    number.append(integer)
    return number[0]


print(find_outlier([1, 2, 4]))
