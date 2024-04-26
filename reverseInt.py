class Solution:
    def reverse(self, x: int) -> int:
        returnValue = ""
        returnSign = "+"

        xString = str(x)
        index = len(xString) - 1
        #print(xString)
        #print("Index: " + str(index))
        for digit in xString:
            #print(xString[index])

            if xString[index] == 0:
                #print("pass, 0")
                pass

            elif xString[index] == "-":
                returnSign = "-"

            elif xString[index] == "+":
                returnSign = "+"

            else:
                returnValue = returnValue + xString[index]

            index = index - 1

        #print(returnValue)

        if returnValue == "":
            returnValue = "0"

        returnInt = int(returnValue)

        if returnSign == "-":
            returnInt = -(returnInt)

        #value goes outside the 32-bit range
        if (returnInt < (-2 ** 31) or returnInt > ((2 ** 31) - 1)):
            returnInt = 0

        return returnInt


x = -123
#x = 120
#x = 123
print(Solution.reverse(Solution, x))