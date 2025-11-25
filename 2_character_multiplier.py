#Create a program that receives two strings on a single line separated by a single space.
#Then, it prints the sum of their multiplied character codes as follows:
#multiply str1[0] with str2[0] and add the result to the total sum, then continue with the next two characters.
#If one of the strings is longer than the other, add the remaining character codes to the total sum without multiplication.


def sum_multiplied_char_codes(input_line):
    str1, str2 = input_line.split()
    total = 0
    min_len = min(len(str1), len(str2))

    # Multiply corresponding character codes
    for i in range(min_len):
        total += ord(str1[i]) * ord(str2[i])

    # Add remaining characters from the longer string
    if len(str1) > len(str2):
        for i in range(min_len, len(str1)):
            total += ord(str1[i])
    elif len(str2) > len(str1):
        for i in range(min_len, len(str2)):
            total += ord(str2[i])

    print(total)

# Example usage:
user_input = input()
sum_multiplied_char_codes(user_input)