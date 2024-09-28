class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, it can't be a substring
        if len(s1) > len(s2):
            return False

        # Create frequency maps for s1 and the first window in s2
        s1map = [0] * 26
        windowMap = [0] * 26
        
        # Fill the frequency map for s1
        for char in s1:
            s1map[ord(char) - ord('a')] += 1

        # Initialize the window map with the first 'len(s1)' characters of s2
        for i in range(len(s1)):
            windowMap[ord(s2[i]) - ord('a')] += 1
        
        # Slide the window across s2
        for i in range(len(s2) - len(s1)):
            # If the current window matches s1map, return True
            if windowMap == s1map:
                return True
            
            # Slide the window: remove the left character and add the next character
            windowMap[ord(s2[i]) - ord('a')] -= 1
            windowMap[ord(s2[i + len(s1)]) - ord('a')] += 1
        
        # Check the last window
        return windowMap == s1map



        