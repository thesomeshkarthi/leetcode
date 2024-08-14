class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}
        bracketStack = []

        for i in s:
            if i in bracketMap:

                if not bracketStack:
                    return False

                value = bracketStack[-1]

                if bracketMap[i] != value:
                    return False
                
                bracketStack.pop()
            else:
                bracketStack.append(i)

        
        return not bracketStack
        