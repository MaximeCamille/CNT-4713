import socket

class Assignment2:

    def __init__(self, age):
        self.age = age

    def sayWelcome(self, name):
        print("Welcome to the assignment, " + name + "!  Haven't seen you for " + str(self.age) + " years!")

    def doubleList(self, input):
        # Create new list
        newList = []

        # First Half
        for i in range(0, len(input)):
            newList.append(input[i] + input[i])

        # Second Half
        for i in range(1, len(input) + 1):
            if i % 2 != 0:
                newList.append(input[i - 1])

        for i in range(1, len(input) + 1):
            if i % 2 == 0:
                newList.append(input[i - 1])
        
        return newList

    def modifyString(self, name):
        newString = ""

        for i in range(1, len(name) + 1):
            if i % 3 == 0:
                newString += name[i - 1].upper()
            elif (i % 4 == 0) and (i % 3 != 0):
                newString += name[i - 1].lower()
            elif (i % 5 == 0) and (i % 4 != 0) and (i % 3 != 0):
                newString += " "
            else:
                newString += name[i - 1]
        
        return newString

    @staticmethod
    def isGoodPassword(password):
        valid = False

        if len(password) < 9:
            return valid

        alphaLow = 0
        alphaUp = 0
        specChar = 0
        alphaNum = 0

        for c in password:
            if c.islower():
                alphaLow += 1
            elif c.isupper():
                alphaUp += 1
            elif c.isdigit():
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

# -----------------------------------------------------------------------------------

obj = Assignment2(24)

obj.sayWelcome("Max")
print(obj.doubleList(["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]))
print(obj.modifyString("abcdefghijklmnopqrstuvwxyz"))

print(obj.isGoodPassword("pgrjgjr&8hr31G"))