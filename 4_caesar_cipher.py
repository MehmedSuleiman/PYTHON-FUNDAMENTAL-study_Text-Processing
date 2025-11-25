#Write a program that returns an encrypted version of the same text.
# Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table.
# For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.

def crypt_text(text):
    lst = []
    crypted_text = ""
    for char in text:
        number_by_ASCII = ord(char)
        lst.append(number_by_ASCII)
    for i in lst:
        new_letter = i +3
        crypted_text += chr(new_letter)

    return crypted_text


string = input()
print(crypt_text(string))
