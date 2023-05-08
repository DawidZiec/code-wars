alp_pos_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}

def alphabet_position(text):
    text2 = text.lower()
    work_tab = []
    final_string = ""
    times = len(text2)
    for letter in range(times):
        if text2[letter] in alp_pos_dict:
            work_tab.append(alp_pos_dict[text2[letter]])
    times2 = len(work_tab)
    for number in range(times2):
        final_string = final_string + str(work_tab[number]) + " "
    return final_string[:-1]

print(alphabet_position("Loot boxes"))