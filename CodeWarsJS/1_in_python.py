

def deleteNth(arr, n):
    rev_arr = arr
    rev_arr.reverse()
    print(rev_arr)
    for t in range(len(rev_arr)):
        occ = rev_arr.count('2')
        if occ > n:
            rev_arr.pop(t)


print(deleteNth([1, 1, 1, 1], 2))  # return [1,1]
print(deleteNth([20, 37, 20, 21], 1))  # return [20,37,21]
print(deleteNth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
