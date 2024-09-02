class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0  
        l = 0  
        char_set = set()  

        # Loop through the string with the right pointer
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            
            char_set.add(s[r])

            # Update the maximum length of substring found
            maxLen = max(maxLen, r - l + 1)

        return maxLen

            



