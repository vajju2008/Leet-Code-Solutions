class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            # Rotate 90 degrees clockwise
            # zip(*mat) transposes the matrix, then [::-1] reverses the rows
            mat = [list(row) for row in zip(*mat[::-1])]
            
        return False