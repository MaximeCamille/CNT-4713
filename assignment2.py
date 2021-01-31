import socket

class Assignment2:

    def __init__(self, age):
        self.age = age

    def sayWelcome(self, name):
        print("Welcome to the assignment, " + name + "!  Haven't seen you for " + self.age + "years!")

    def doubleList(self, input):
        # Create new list
        newList = []

        # First Half
        for i in range(0, len(newList)):
            newList.append(input[i] + input[i])

        # Second Half
        for i in range(0, len(newList)):
            if i % 2 != 0:
                newList.append(input[i])

        for i in range(0, len(newList)):
            if i % 2 == 0:
                newList.append(input[i])

    def modifyString(self, name):
        newString = ""

        for i in range(1, len(name)):
            if i % 3 == 0:
                newString += name[i - 1].upper()
            elif (i % 4 == 0) and (i % 3 != 0):
                newString += name[i - 1].lower()
            elif (i % 5 == 0) and (i % 4 != 0) and (i % 3 != 0):
                newString += " "
        
        return newString

    def isGoodPassword(self, password):
        valid = False

        if len(password) < 9:
            return valid

        alphaLow = 0
        alphaUp = 0
        specChar = 0
        alphaNum = 0

        for c in password:
            if c.isLower():
                alphaLow += 1
            elif c.isUpper():
                alphaUp += 1
            elif c.isDigit():
                alphaNum += 1
            elif c == '.' or c == ',' or c == '#' or c == '(':
                specChar += 1

        if (alphaLow >= 2 or alphaUp >= 3) and (specChar >= 2 or alphaNum >= 1):
            valid = True

        return valid

    def connectTcp(self, host, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                print("Connection successfully established")
                sock.close()
            return True
        except socket.error as err:
            print("Socket error, connection faild: %s" % err)
            return False