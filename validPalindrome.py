class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Take a string and return a new one with only lower-case, alphanumeric characters from the parameter string
        def stripLetters(s: str):
            newString = ""
            for character in s:
                character = character.lower()
                asciiChar = ord(character)
                if (asciiChar <= 57 and asciiChar >= 48) or (asciiChar <= 122 and asciiChar >= 97):
                    newString = newString + character

            return newString

        s = stripLetters(s)
        #print("New s: " + s)
        pos1 = 0
        pos2 = len(s) - 1
        
        #If the given input string is empty
        if s == "":
            return True

        searching = True
        while(searching):
            char1 = s[pos1]
            char2 = s[pos2]

            #Compare characters
            if char1 != char2:
                searching = False
                return False
            else:
                #print("characters are the same")

                #If at the middle value
                if pos1 == pos2:
                    #print("odd")
                    searching = False
                    return True
                #If the string is an even length and you're at the two middle values
                elif (len(s) % 2) == 0 and (pos1 + 1) == pos2:
                    pos1 = pos1 + 1
                    pos2 = pos2 - 1        

                    #Compare values
                    if char1 != char2:
                        searching = False
                        return False
                    else:
                        searching = False
                        return True
                else:
                    #Move to the next values
                    #print("increment positions")
                    pos1 = pos1 + 1
                    pos2 = pos2 - 1
                