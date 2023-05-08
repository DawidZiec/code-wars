def odd_or_even(arr):
    result = sum(arr)
    if result % 2 == 0:
        return "even"
    else:
        return "odd"