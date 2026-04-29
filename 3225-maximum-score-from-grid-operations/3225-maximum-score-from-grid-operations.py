class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pref[j][i + 1] = pref[j][i] + grid[i][j]
        




        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        for curr_paint in range(n + 1):
            dp[0][curr_paint] = 0
            
        for j in range(n):
            next_dp = [[-1] * (n + 1) for _ in range(n + 1)]
            
            for curr_paint in range(n + 1):
                pref_max = [-1] * (n + 1)
                cur_max = -1
                for prev_paint in range(n + 1):
                    if dp[prev_paint][curr_paint] != -1 and dp[prev_paint][curr_paint] > cur_max:
                        
                        cur_max = dp[prev_paint][curr_paint]
                    pref_max[prev_paint] = cur_max
                    
                suff_max = [-1] * (n + 2)
                cur_max = -1
                for prev_paint in range(n, -1, -1):
                    val = dp[prev_paint][curr_paint]
                    if val != -1:
                        coins_grabbed = pref[j][prev_paint] - pref[j][curr_paint] if prev_paint > curr_paint else 0
                        if val + coins_grabbed > cur_max:
                            cur_max = val + coins_grabbed
                    suff_max[prev_paint] = cur_max
                    
                for next_paint in range(n + 1):
                    res = -1
                    
                    pm = pref_max[next_paint]
                    if pm != -1:
                        coins_grabbed = pref[j][next_paint] - pref[j][curr_paint] if next_paint > curr_paint else 0
                        if pm + coins_grabbed > res:
                            res = pm + coins_grabbed
                            
                    sm = suff_max[next_paint + 1]
                    if sm != -1 and sm > res:
                        res = sm
                        
                    next_dp[curr_paint][next_paint] = res
            
            dp = next_dp
            
        ans = 0
        for curr_paint in range(n + 1):
            if dp[curr_paint][0] > ans:
                ans = dp[curr_paint][0]
                
        return ans