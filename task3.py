import hashlib
import sys
import random

#Creating this boolean to tell the code whether we are using file type 2 or file type 3
type2 = True
mylist = []

def getPass(list):
    temp = ""
    for x in range(0,len(list)):
        temp+=str(list[x])

    return temp

def checkFile2(password):
    file = open("file2","r")

    tempVal = hashlib.sha256(password.encode())
    hashPass = str(tempVal.hexdigest())

    for line in file:
        vS = line.split(',')
        if(hashPass == vS[1]):
            print(str(password +" is a password found for the username: "+vS[0]))
            return


def checkFile3(password):
    file = open("file3","r")

    tempVal = hashlib.sha256(password.encode())
    hashPass = str(tempVal.hexdigest())

    for line in file:
        vS = line.split(',')


        tempVal = hashlib.sha256(password.encode())
        hashPass = str(tempVal.hexdigest())

        if(hashPass == vS[2]):
            salt = password[len(password)-1]
            password = password[:-1]
            print(str(password +" is a password found for the username: "+vS[0]))
            return



mylist.append(0)
password = ""
while(len(mylist)<8):
    password = getPass(mylist)
    checkFile2(password)
    mylist[0] += 1

    for y in range(0, len(mylist)):
        if((y + 1) == len(mylist)):
            if(mylist[y] == 10):
                mylist[y] = 0
                mylist.append(0)
        else:
            if(mylist[y] == 10):
                mylist[y] = 0
                mylist[y+1] += 1
