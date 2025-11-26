#Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
#The input will be provided as a single string.



def find_emoticons(string):
    new_string = sting.replace('.', ' ')
    words = new_string.split()
    emoticons = []
    for character in words:
        if ":" in character:
            emoticon = character
            emoticons.append(emoticon)


    return emoticons


sting = input()
for emoticon in find_emoticons(sting):
    print(emoticon)