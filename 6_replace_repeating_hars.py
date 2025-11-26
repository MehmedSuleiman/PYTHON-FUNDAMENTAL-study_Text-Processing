#Write a program that reads a string from the console and
#replaces any sequence of the same letters with a single corresponding letter.


def replace_repeating_chars(string):
    if not string:  # handle empty input
        return ""

    new_string = [string[0]]  # start with the first character

    for letter in string[1:]:
        if letter != new_string[-1]:  # only add if different from the last appended
            new_string.append(letter)

    return ''.join(new_string)


# Read input and print result
print(replace_repeating_chars(input()))