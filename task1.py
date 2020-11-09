import hashlib
import sys

def verifyUserName(userName):
    file = open("file1","r")

    for line in file:
        uN = line.split(',')
        if(userName == uN[0]):
            print("That username is already taken.")
            return False


# initializing string
again = True

while(again):
    answer = input("Enter c to create and account, l to login, or any other value to quit.")
    if(answer == 'c'):
        validUser = False
        while(validUser == False):
            userName = input("Please enter a username: ")
            validUser = verifyUserName(userName)

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
