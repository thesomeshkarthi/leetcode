class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        integerMap = {}

        for i, n in enumerate(nums):
            value = target - n
            if value in integerMap:
                return [integerMap[value], i]
            else:
                integerMap[n] = i
        return 