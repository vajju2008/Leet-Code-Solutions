class Solution:
    def minimumDistance(self, word: str) -> int:
        def get_dist(a: int, b: int) -> int:
            if a == 26: 
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        # Dictionary mapping other_finger_position -> min_cost
        # 26 represents the initial "free" finger state
        dp = {26: 0} 
        prev = 26

        for char in word:
            c = ord(char) - 65
            new_dp = {}

            for other, cost in dp.items():
                # Option 1: Move the 'prev' finger to 'c'. The 'other' finger stays put.
                cost1 = cost + get_dist(prev, c)
                new_dp[other] = min(new_dp.get(other, float('inf')), cost1)

                # Option 2: Move the 'other' finger to 'c'. 'prev' becomes the new 'other' finger.
                cost2 = cost + get_dist(other, c)
                new_dp[prev] = min(new_dp.get(prev, float('inf')), cost2)

            dp = new_dp
            prev = c

        return min(dp.values())