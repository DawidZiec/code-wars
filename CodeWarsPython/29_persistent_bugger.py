# Input: 142
# Output: 1, because 1*4*2=8, which is a single digit number
# Input: 295
# Output: 2, because 2*9*5=90, 9*0=0, which is a single digit number

def persistence(n):
    number = n
    iter = 0
    while True:
        multi = 1
        if (number/10)<1:
            break
        digits = [char for char in str(number)]
        for t in range(len(digits)):
            multi=multi*int(digits[t])
        number = (multi)
        iter+=1
    return iter

print(persistence(957))