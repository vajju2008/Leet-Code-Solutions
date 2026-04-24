class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count("R") - moves.count("L")) + moves.count("_")