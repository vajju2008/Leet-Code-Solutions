class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions: 0: North, 1: East, 2: South, 3: West
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        # We use a set of tuples for O(1) lookups. 
        # Lists aren't hashable, so we convert each obstacle [x, y] to (x, y).
        obstacle_set = {tuple(o) for o in obstacles}
        
        x, y = 0, 0
        di = 0  # Start facing North (index 0)
        max_sq_dist = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn Left 90 degrees
                di = (di - 1) % 4
            elif cmd == -1:  # Turn Right 90 degrees
                di = (di + 1) % 4
            else:
                # Move 'cmd' steps one by one to check for obstacles
                for _ in range(cmd):
                    nx, ny = x + dx[di], y + dy[di]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        # Update the maximum squared Euclidean distance reached
                        max_sq_dist = max(max_sq_dist, x*x + y*y)
                    else:
                        # Obstacle hit; stop moving for this command
                        break
                        
        return max_sq_dist