from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        arr = sorted(zip(robots, distance), key=lambda x: x[0])
        walls.sort()
        
        prev_dp = [0, 0]
        
        for i in range(n):
            curr_dp = [0, 0]
            
            left = arr[i][0] - arr[i][1]
            if i > 0:
                left = max(left, arr[i - 1][0] + 1)
            
            l = bisect_left(walls, left)
            r = bisect_right(walls, arr[i][0])
            count_left = r - l if r > l else 0
            ans_left = prev_dp[0] + count_left
            
            for j in (0, 1):
                right = arr[i][0] + arr[i][1]
                if i + 1 < n:
                    if j == 0:
                        right = min(right, arr[i + 1][0] - arr[i + 1][1] - 1)
                    else:
                        right = min(right, arr[i + 1][0] - 1)
                
                right = max(right, arr[i][0])
                
                l2 = bisect_left(walls, arr[i][0])
                r2 = bisect_right(walls, right)
                count_right = r2 - l2 if r2 > l2 else 0
                
                ans_right = prev_dp[1] + count_right
                curr_dp[j] = max(ans_left, ans_right)
            
            prev_dp = curr_dp
            
        return prev_dp[1]