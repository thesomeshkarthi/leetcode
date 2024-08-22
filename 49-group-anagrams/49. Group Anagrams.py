class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}

        for word in strs:
            alphaWord = ''.join(sorted(word))
            if alphaWord in anagramMap:
                #append word to list associated with sorted(word) key
                anagramMap[alphaWord].append(word)
            else:
                #create entry in anagramMap
                tempList = []
                tempList.append(word)
                anagramMap[alphaWord] = tempList

        sol = []
        for key in anagramMap:
            sol.append(anagramMap[key])

        return sol

        