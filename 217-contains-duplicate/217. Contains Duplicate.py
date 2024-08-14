class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenNumbers = set()

        for n in nums:
            if n in seenNumbers:
                return True
            seenNumbers.add(n)
        return False 