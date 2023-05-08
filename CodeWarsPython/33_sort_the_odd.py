def sort_array(source_array):
    number =[]
    index = []
    for i in range(len(source_array)):
        if source_array[i]%2 != 0:
            number.append(source_array[i])
            index.append(i)
    number.sort()
    for n in range(len(index)):
        source_array[index[n]]= number[n]
    return source_array

print(sort_array([5, 8, 6, 3, 4]))
