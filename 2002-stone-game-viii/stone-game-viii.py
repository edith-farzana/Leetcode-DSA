from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        total_sum = sum(stones)
        dp = total_sum
        
        for i in range(n - 1, 1, -1):
            total_sum -= stones[i]
            if total_sum - dp > dp:
                dp = total_sum - dp
                
        return dp
