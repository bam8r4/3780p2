import hashlib
import sys
import random

def verifyUserName(userName):
    file = open("file1","r")

    if(userName.isalpha()):
        if(len(userName) > 10 or len(userName) < 1):
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

def checkFile1(username, password):
    file = open("file1","r")

    for line in file:
        vS = line.split(',')
        if(username == vS[0]):
            if(password == vS[1]):
                print("File 1 login success.")
                return

    print("Improper username or password for file 1")
    return


def checkFile2(username, password):
    file = open("file2","r")

    tempVal = hashlib.sha256(password.encode())
    hashPass = str(tempVal.hexdigest())

    for line in file:
        vS = line.split(',')
        if(username == vS[0]):

            if(hashPass == vS[1]):
                print("File 2 login success.")
                return

    print("Improper username or password for file 2.")
    return


def checkFile3(username, password):
    file = open("file3","r")

    tempVal = hashlib.sha256(password.encode())
    hashPass = str(tempVal.hexdigest())

    for line in file:
        vS = line.split(',')
        if(username == vS[0]):
            salt = vS[1]
            password += salt

            tempVal = hashlib.sha256(password.encode())
            hashPass = str(tempVal.hexdigest())

            if(hashPass == vS[2]):
                print("File 3 login success.")
                return

    print("Improper username or password for File 3")
    return

# initializing string
again = True

while(again):
    answer = input("Enter c to create and account, l to login, or any other value to quit. ")
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

        outPut1 = open("file1","a+")
        outPut2 = open("file2","a+")
        outPut3 = open("file3","a+")

        outPut1.write(userName+","+str(password)+",\n")

        tempVal = hashlib.sha256(password.encode())
        outPut2.write(userName+","+str(tempVal.hexdigest())+",\n")

        saltedPass = password+str(salt)
        tempVal = hashlib.sha256(saltedPass.encode())
        outPut3.write(userName+","+str(salt)+","+tempVal.hexdigest()+",\n")

        outPut1.close()
        outPut2.close()
        outPut3.close()

    elif(answer == 'l'):
        username = input("Please input your username: ")
        password = input("Please input your password: ")

        checkFile1(username, password)
        checkFile2(username, password)
        checkFile3(username, password)

    else:
        print("Goodbye.")
        exit()
