from typing import List

class Solution:
    #Write a function to find the longest common prefix string amongst an array of strings.
    #If there is no common prefix, return an empty string "".
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestStringLength = len(strs[0])
        for string in strs:
            length = len(string)
            if length < shortestStringLength:
                shortestStringLength = length

        prefixString = ""
        for index in range(shortestStringLength):
            #print(index)
            currentChar = strs[0][index]
            for nextString in strs:
                #print(nextString)
                #print(nextString[index])

                if currentChar != nextString[index]:
                    return prefixString
            

            #print("Adding " + currentChar + " to prefixString")
            prefixString = prefixString + currentChar
            index = index + 1

        return prefixString

strs = ["do","dogeracecar","dogecar"]
print(Solution.longestCommonPrefix(Solution, strs))