import hashlib
import sys
import random

def generateSalt():
    return random.randint(0,9)

numOfUsers = int(input("Enter number of users: "))
lowerBound = int(input("Enter lower bound for password length: "))
upperBound = int(input("Enter upper bound for password length: "))


outPut1 = open("file1","w")
outPut2 = open("file2","w")
outPut3 = open("file3","w")

for x in range(0,numOfUsers):

    username = "user"+str(x)
    passLength = random.randint(lowerBound,upperBound)
    password = ""
    
    for y in range(0,passLength):
        password += str(random.randint(0,9))

    salt = generateSalt()

    outPut1.write(username+","+str(password)+",\n")

    tempVal = hashlib.sha256(password.encode())
    outPut2.write(username+","+str(tempVal.hexdigest())+",\n")

    saltedPass = password+str(salt)
    tempVal = hashlib.sha256(saltedPass.encode())
    outPut3.write(username+","+str(salt)+","+tempVal.hexdigest()+",\n")

outPut1.close()
outPut2.close()
outPut3.close()
