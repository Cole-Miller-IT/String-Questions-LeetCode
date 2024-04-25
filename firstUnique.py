class Solution:
    def alreadySeen(s, seenList):
        for character in seenList:
            if s == character:
                return True
            
        return False

    def firstUniqChar(self, s: str) -> int:
        index = 0
        seenList = ""
        for char1 in s:
            unique = True
            #print(char1)
            
            if self.alreadySeen(char1, seenList) == True:
                #print(char1 + " already seen")
                index = index + 1
                continue

            for char2 in s[index + 1:len(s)]:
                #print("Comparing: " + char1 + " and " + char2)
                if char1 == char2:
                    
                    #print(char1 + " is not unique")
                    #print(char1)
                    #print(char2)
                    unique = False
                    seenList = seenList + char1
                    break

            

            if unique == True:
                print(char1 + " is unique")
                #print(index + 1)
                return index
            
            index = index + 1

        return -1 #If no unique characters
                



s = "clloeetcodet"
print(Solution.firstUniqChar(Solution, s))