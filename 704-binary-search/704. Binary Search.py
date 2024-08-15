class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right :
            mid = int((right + left) / 2)
            midValue = nums[mid]

            if midValue > target:
                right = mid - 1
            elif midValue < target:
                left = mid + 1
            elif midValue == target:
                return mid

        return -1
                
        