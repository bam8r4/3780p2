import hashlib
import sys
import random

def verifyUserName(userName):
    file = open("file1","r")

    if(userName.isalpha()):
        if(len(userName) != 10):
            print("Username is not an appropriate length. Must be 10 characters long.")
            return False
    else:
        print("Username must be alphabetical characters only.")
        return False

    for line in file:
        uN = line.split(',')
        if(userName == uN[0]):
            print("That username is already taken.")
            return False

    return True

def verifyPassword(password):
    if(password.isdecimal()):
        return True
    else:
        print("Password can be any length but must be all integers.")
        return False

def generateSalt():
    return random.randint(0,10)


# initializing string
again = True

while(again):
    answer = input("Enter c to create and account, l to login, or any other value to quit.")
    if(answer == 'c'):
        validUser = False
        validPassword = False

        while(validUser == False):
            userName = input("Please enter a username: ")
            validUser = verifyUserName(userName)

        while(validPassword == False):
            password = input("Please enter a password made of only integers: ")
            validPassword = verifyPassword(password)

        salt = generateSalt()

    elif(answer == 'l'):
        print("loggin in")
    else:
        print("Goodbye.")
        exit()


str = input("Type value to be hashed: ")

# encoding GeeksforGeeks using encode()
# then sending to SHA256()
result = hashlib.sha256(str.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA256 is : ")
print(result.hexdigest())

count += 1
print ("\r")
