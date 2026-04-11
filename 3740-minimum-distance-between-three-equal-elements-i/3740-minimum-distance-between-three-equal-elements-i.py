from collections import defaultdict
from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        # Group indices by their values
        for i, num in enumerate(nums):
            indices[num].append(i)
        min_dist = float('inf')
        # Evaluate each group
        for pos in indices.values():
            m = len(pos)
            if m >= 3:
                # Sliding window of size 3 over the indices
                for i in range(m - 2):
                    dist = 2 * (pos[i + 2] - pos[i])
                    min_dist = min(min_dist, dist)
                    
        return min_dist if min_dist != float('inf') else -1