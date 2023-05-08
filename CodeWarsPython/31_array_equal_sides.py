def find_even_index(arr):
    for i in range(len(arr)):
        left, right = 0, 0
        sub_left = arr[:i]
        sub_right = arr[i+1:]
        left = sum(sub_left)
        right = sum(sub_right)
        if left == right:
            return i
    return -1

print(find_even_index([1, 2, 3, 4, 3, 2, 1]))