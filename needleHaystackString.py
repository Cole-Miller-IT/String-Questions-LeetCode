class Solution:
    #Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    def strStr(self, haystack: str, needle: str) -> int:
        needleIndex = 0
        firstNeedleChar = needle[needleIndex]
        hayIndex = 0
        needleLength = len(needle)

        if needleLength > len(haystack):
            return -1

        for hayChar in haystack:
            if firstNeedleChar == hayChar:
                firstOccuranceIndex = hayIndex
                index = hayIndex + 1

                for nextNeedleChar in needle[1:needleLength]:
                    if needleLength > len(haystack[hayIndex:len(haystack)]):
                        firstOccuranceIndex = -1
                        break

                    nextHayChar = haystack[index]
                    if nextNeedleChar != nextHayChar:
                        #not a full match
                        #print(nextNeedleChar + " and " + nextHayChar + " not a match")
                        firstOccuranceIndex = -1
                        break

                    #print(nextNeedleChar + " and " + nextHayChar + " a match")

                    index = index + 1


                if firstOccuranceIndex != -1:
                    #print("needle found")
                    return firstOccuranceIndex

            #move onto the next hayChar
            hayIndex = hayIndex + 1

        return -1


haystack = "missisippi"
needle = "issipi"

print(Solution.strStr(Solution, haystack, needle))