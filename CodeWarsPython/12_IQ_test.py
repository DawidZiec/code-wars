'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples:
# Third number is odd, while the rest of the numbers are even
iq_test("2 4 7 8 10") => 3

# Second number is even, while the rest of the numbers are odd
iq_test("1 2 1 1") => 2
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


def iq_test(numbers):
    integers = numbers.split(' ')
    passing = []
    for integer in integers:
        passing.append(int(integer))
    number = []
    if odd_or_even(passing) == 'odd':
        while len(number) == 0:
            for integer in passing:
                if integer % 2 == 0:
                    number.append(integer)
    else:
        while len(number) == 0:
            for integer in passing:
                if integer % 2 == 1:
                    number.append(integer)
    to_print = passing.index(number[0])
    return to_print+1


print(iq_test("1 1 4"))
