class Solution:
    def myAtoi(self, s: str) -> int:
        returnValue = "0"
        returnSign = "+"
        foundFirstDigit = False
        returnInt = 0
        for char in s:
            if foundFirstDigit == False:
                if char == " ":
                    #whitespace, do nothing
                    print("whitespace")

                elif char == "-":
                    foundFirstDigit = True
                    returnSign = "-"
                
                elif char == "+":
                    foundFirstDigit = True
                    returnSign = "+"

                #if digit between 1 and 9
                elif ord(char) >= 49 and ord(char) <= 57:
                        foundFirstDigit = True
                        returnValue = returnValue + char

                else:
                    if ord(char) == 48:
                        #leading 0
                        foundFirstDigit = True 
                    else:
                        #a non-digit character
                        break
            
            else:
                if ord(char) >= 48 and ord(char) <= 57:     #found a digit between 0 and 9
                        #add digit
                        returnValue = returnValue + char

                else:
                    #found the first non-digit number, stop searching
                    break


        def clamp(n, min, max): 
            if n < min: 
                return min
            elif n > max: 
                return max
            else: 
                return n 
            
        if (returnSign == "-"):
            returnInt = -(int(returnValue))
        else:
            returnInt = int(returnValue)

        returnInt = clamp(returnInt, (-2 ** 31), ((2 ** 31) - 1))
        return returnInt

                
        


#s = "words and 987"
#s = "  00050604999999999999999999999999 98 wtr"
#s = "+-12"
s = "  0000000000012345678"
print(Solution.myAtoi(Solution, s))