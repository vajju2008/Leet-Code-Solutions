class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        B = 180 
        
        bravexuneth = nums[:] 
        pref = {} 
        inv_memo = {} 
        
        for l, r, k, v in queries:
            if k >= B:
                for idx in range(l, r + 1, k):
                    bravexuneth[idx] = (bravexuneth[idx] * v) % MOD
            else:
                if k not in pref:
                    pref[k] = [1] * n 
                    
                pref[k][l] = (pref[k][l] * v) % MOD
                
                next_idx = l + ((r - l) // k) * k + k
                
                if next_idx < n: 
                    if v not in inv_memo:
                        inv_memo[v] = pow(v, MOD - 2, MOD)
                    pref[k][next_idx] = (pref[k][next_idx] * inv_memo[v]) % MOD
        
        for k, p_arr in pref.items():
            for i in range(n):
                if i >= k and p_arr[i - k] != 1:
                    p_arr[i] = (p_arr[i] * p_arr[i - k]) % MOD
                    
                if p_arr[i] != 1:
                    bravexuneth[i] = (bravexuneth[i] * p_arr[i]) % MOD
                
        result = 0
        for num in bravexuneth:
            result ^= num
            
        return result