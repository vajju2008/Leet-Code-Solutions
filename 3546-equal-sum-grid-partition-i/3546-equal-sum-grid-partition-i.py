class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        # 1. Calculate the total sum
        total_sum = 0
        for row in grid:
            total_sum += sum(row)
            
        # If the total sum is odd, we can't split it into two equal integers
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # 2. Check Horizontal Cuts (Row-wise)
        current_horizontal_sum = 0
        for i in range(n - 1): # n is number of rows
            current_horizontal_sum += sum(grid[i])
            if current_horizontal_sum == target:
                return True
                
        # 3. Check Vertical Cuts (Column-wise)
        current_vertical_sum = 0
        for j in range(m - 1): # m is number of columns
            col_sum = 0
            for i in range(n):
                col_sum += grid[i][j]
            
            current_vertical_sum += col_sum
            if current_vertical_sum == target:
                return True
        
        # THIS IS THE MISSING PART:
        # If we checked every possible cut and found nothing, return False
        return False