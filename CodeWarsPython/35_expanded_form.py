def expanded_form(num):
    numbers = []
    index = []
    work_operator = str(num)
    rev_wo = work_operator[::-1]
    split_rev_wo = [x for x in rev_wo]
    for i in range(len(split_rev_wo)):
        if split_rev_wo[i] != '0':
            numbers.append(split_rev_wo[i])
            index.append(i)
    for t in range(len(numbers)):
        for u in range(index[t]):
            numbers[t]=numbers[t]+"0"
    correct_order = numbers[::-1]
    temp_to_return = ''
    for n in range(len(correct_order)):
        temp_to_return = temp_to_return + correct_order[n] + ' + '
    string_to_return = temp_to_return[:-3]
    return string_to_return

print(expanded_form(2001040))