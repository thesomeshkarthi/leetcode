class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0 
        r = len(matrix) - 1

        while l <= r: 
            mid = (l + r) // 2 
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                return True
        
        left = 0 
        right = len(matrix[r]) - 1

        while left <= right:
            middle = (left + right) // 2
            if matrix[r][middle] > target:
                right = middle - 1
            elif matrix[r][middle] < target:
                left = middle + 1
            else:
                return True
        
        return False
        
