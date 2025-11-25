#Write a program that reads usernames on a single line (separated by ", ") and
# prints all valid usernames on separate lines.
#A valid username:
#•	has length between 3 and 16 characters inclusive
#•	can contain only letters, numbers, hyphens, and underscores
#•	has no redundant symbols before, after, or in between

usernames = input().split(", ")

def is_valid_username(i):
    if 3 < len(i) < 16:
        if i.isalnum()  or "-" in i or "_" in i :
            print(i)
        else:
            return False
    else:
        return False

for username in usernames:
    is_valid_username(username)