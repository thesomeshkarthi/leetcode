class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1map = {}
        for char in s1:
            if char in s1map:
                s1map[char] += 1
            else:
                s1map[char] = 1
        
        l = 0
        r = 0

        while r <= len(s2) - 1:
            while r <= len(s2) - 1 and s2[r] not in s1map:
                r += 1
            l = r
            nextStart = r + 1
            r += (len(s1) - 1)

            if r > len(s2) - 1:
                return False

            temp = s1map.copy()
            resultFound = True

            while l <= r:
                if s2[l] not in temp:
                    resultFound = False
                    break
                if temp[s2[l]] == 0:
                    resultFound = False
                    break

                temp[s2[l]] -= 1
                l += 1 
            
            if resultFound:
                return True
            

            if nextStart > len(s2) - 1:
                return False
            r = nextStart
            l = nextStart
        
        return False



        