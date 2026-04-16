from typing import List
from collections import defaultdict
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i) 
        min_dist = [-1] * n
        
        for indices in pos.values():
            m = len(indices)
            if m > 1:
                for i in range(m):
                    curr = indices[i]
                    prev_idx = indices[i - 1]
                    next_idx = indices[(i + 1) % m]
                    
                    d1 = abs(curr - prev_idx)
                    d1 = min(d1, n - d1)
                    
                    d2 = abs(curr - next_idx)
                    d2 = min(d2, n - d2)
                    
                    min_dist[curr] = min(d1, d2)
                    
        return [min_dist[q] for q in queries]