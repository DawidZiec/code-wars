# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    word = text.lower()
    singles = []
    doubles = []
    for letter in word:
        if (letter in singles) == False:
            singles.append(letter)
        elif (letter in doubles) == False:
            doubles.append(letter)
    return len(doubles)
