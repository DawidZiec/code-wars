"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to
the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is
to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""


def snail(snail_map):
    n = len(snail_map)
    to_print = []

    while len(snail_map) > 0:

        # this handles left to right
        for item in snail_map[0]:
            to_print.append(item)
        del snail_map[0]
        if len(snail_map) == 0:
            break

        # this handles top to bottom
        for item in snail_map:
            to_print.append(item.pop())

        # this handles right to left
        temp1 = []
        for item in snail_map[-1]:
            temp1.append(item)
        del snail_map[-1]
        temp1.reverse()
        for item in temp1:
            to_print.append(item)

        # this handles bottom to top
        temp2 = []
        for item in snail_map:
            temp2.append(item.pop(0))
        temp2.reverse()
        for item in temp2:
            to_print.append(item)

    print(snail_map)
    print(to_print)


snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
      [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
