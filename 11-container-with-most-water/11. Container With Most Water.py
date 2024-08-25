class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                smaller = l
            else:
                smaller = r
            
            area = height[smaller] * (r - l)

            if area > res:
                res = area
            
            if smaller == l:
                l += 1
            elif smaller == r:
                r -= 1
        
        return res


            
            
        