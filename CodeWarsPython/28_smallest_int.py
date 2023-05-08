def find_smallest_int(arr):
    while len(arr)>1:
        if arr[0] >= arr[1]:
            arr.pop(0)
        else:
            arr.pop(1)
    return arr[0]

print(find_smallest_int([1, 14, 28]))