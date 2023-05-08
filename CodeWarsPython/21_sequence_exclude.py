def remov_nb(n):
    sequence = []
    for i in range(1, n+1):
        sequence.append(i)
    sum = 0
    to_return = []
    for j in sequence:
        sum = sum + j
    for k in sequence:
        for l in sequence:
            if k*l == sum - k - l:
                result = (k, l)
                to_return.append(result)
    return to_return

print(remov_nb(26))