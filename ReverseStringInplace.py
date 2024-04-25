import math
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        index1 = 0
        index2 = len(s) - 1
        for character in s:
            #print("Before swap: ")
            #print(s[index1])
            #print(s[index2])
            
            tempVar = character
            
            s[index1] = s[index2]
            s[index2] = tempVar

            #print("After swap: ")
            #print(s[index1])
            #print(s[index2])
            
            index1 = index1 + 1
            index2 = index2 - 1
            
            if (index1 >= math.ceil(len(s) / 2)):
                print(index1)
                break
            
        print(s)
        

s = ["h","e","l","l","o"]
Solution.reverseString(Solution, s)