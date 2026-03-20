class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        prefX = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefY = [[0] * (cols + 1) for _ in range(rows + 1)]
        ans = 0

        for r in range(rows):
            for c in range(cols):
                valX = 1 if grid[r][c] == 'X' else 0
                prefX[r+1][c+1] = valX + prefX[r][c+1] + prefX[r+1][c] - prefX[r][c]   
                valY = 1 if grid[r][c] == 'Y' else 0
                prefY[r+1][c+1] = valY + prefY[r][c+1] + prefY[r+1][c] - prefY[r][c]
                if prefX[r+1][c+1] == prefY[r+1][c+1] and prefX[r+1][c+1] > 0:
                    ans += 1
                    
        return ans