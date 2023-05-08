# Your task is to make a function that can take


def descending_order(num):
    # prep work
    alpha = str(num)
    parsed_alpha = list(alpha)
    int_parsed_alpha = []

    # creating array with parsed and converted to ints digits
    for i in range(len(parsed_alpha)):
        int_parsed_alpha.append(int(parsed_alpha[i]))

    # bubble sorting the digits in the ascending order
    for j in range(len(int_parsed_alpha)-1, 0, -1):
        for k in range(j):
            if int_parsed_alpha[k] > int_parsed_alpha[k+1]:
                temp = int_parsed_alpha[k]
                int_parsed_alpha[k] = int_parsed_alpha[k+1]
                int_parsed_alpha[k+1] = temp

    # reversing the order
    reversed_ipa = int_parsed_alpha[::-1]

    # merging the digits back together
    merged = ""
    for n in range(len(reversed_ipa)):
        merged = merged + str(reversed_ipa[n])

    return(int(merged))


print()
print(descending_order(18024))
print()
