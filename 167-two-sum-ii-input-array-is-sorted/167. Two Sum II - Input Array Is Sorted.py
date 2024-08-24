class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        integerMap = {}

        for i, n in enumerate(numbers):
            value = target - n
            if value in integerMap:
                return [integerMap[value] + 1, i + 1]
            else:
                integerMap[n] = i
        return 