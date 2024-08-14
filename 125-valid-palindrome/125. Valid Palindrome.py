class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''.join(char for char in s if char.isalnum())
        clean_s = clean_s.lower()

        left = 0
        right = len(clean_s) - 1

        while left <= right:
            if(clean_s[left] != clean_s[right]):
                return False
            left = left + 1
            right = right - 1
        
        return True
        