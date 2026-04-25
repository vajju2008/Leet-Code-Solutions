class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        
        def get_1d_distance(x, y, s):
            if y == 0:
                return x
            elif x == s:
                return s + y
            elif y == s:
                return 2 * s + (s - x)
            else:
                return 3 * s + (s - y)
                
        arr = []
        for x, y in points:
            arr.append(get_1d_distance(x, y, side))
        arr.sort()
        
        N = len(arr)
        
        arr2 = arr + [v + 4 * side for v in arr]
        
        next_idx = [2 * N] * (2 * N + 1)
        
        def check(mid):
            j = 0
            for i in range(2 * N):
                while j < 2 * N and arr2[j] - arr2[i] < mid:
                    j += 1
                next_idx[i] = j
                
            for i in range(N):
                curr = i
                target = i + N  
                
                for _ in range(k - 1):
                    curr = next_idx[curr]
                    if curr >= target:
                        break
                else:
                    if arr2[target] - arr2[curr] >= mid:
                        return True
                        
            return False

        low = 1
        high = (4 * side) // k
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if check(mid):
                ans = mid
                low = mid + 1  
            else:
                high = mid - 1 
                
        return ans