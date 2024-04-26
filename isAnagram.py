class Solution:
    #Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    def isAnagram(self, s: str, t: str) -> bool:
        lengthS = len(s)
        if len(t) != lengthS:
            print("Not same length")
            return False
        
        for charT in t:
            print("Looking for " + charT + " in " + s)
            found = False
            index = 0
            for charS in s:
                #print(charT)
                #print(charS)
                
                if charT == charS:
                    #Remove value from s
                    #print("match")
                    #print("index: " + str(index))
                    


                    firstString = s[0:index]
                    secondString = s[index + 1:lengthS]

                    #print("first string: " + s[0:index])
                    #print("second string: " + s[index + 1:lengthS])
                    s = firstString + secondString
                    print("New s: " + s)
                    
                    found = True
                    break

                index = index + 1

            #Couldn't find the value
            if found == False:
                return False

        #Used every value
        return True


s = "abba"
t = "baba"
print(Solution.isAnagram(Solution, s, t))