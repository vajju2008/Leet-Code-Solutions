class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0
        j = n - 1 

        while colors[0] == colors[j]:
            j -= 1 
        while colours[-1] == colors[i]:
            i +=1
        return max(j, n - 1 - i)
