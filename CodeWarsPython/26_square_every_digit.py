from cmath import sqrt


def square_digits(num):
    string_version = str(num)
    times = len(string_version)
    final_tab = []
    final_str = ""
    for digit in range(times):
        final_tab.append((int(string_version[digit]))**2)
    for square in range (times):
        final_str = final_str+str(final_tab[square])
    return int(final_str)

print(square_digits(158))