class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        res = 5001

        while l < r:
            mid = (l + r) // 2
            numsMid = nums[mid]

            res = min(res, numsMid)

            if numsMid > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        

        return min(res, nums[l])
        



        # 8 1 2 3 4 5