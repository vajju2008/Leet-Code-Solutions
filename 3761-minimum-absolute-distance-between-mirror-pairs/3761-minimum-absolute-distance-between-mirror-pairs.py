class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        prev = dict()
        ans = inf
        for i, num in enumerate(nums):
            if num in prev:
                ans = min(ans, i - prev[num])
            prev[int(str(num)[::-1])] = i
        return -1 if ans == inf else ans