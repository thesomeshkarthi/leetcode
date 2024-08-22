class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberMap = {}

        for num in nums:
            if num in numberMap:
                numberMap[num] += 1
            else:
                numberMap[num] = 1
        
        sortedNumberMap = sorted(numberMap.items(), key=lambda item: item[1], reverse=True)

        sol = []
        i = 0
        while i < k:
            sol.append(sortedNumberMap[i][0])
            i += 1
        
        return sol



        