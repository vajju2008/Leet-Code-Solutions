class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        # Combine all attributes along with the original index to restore order later
        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        
        # Sort robots by position to process them from left to right
        robots.sort(key=lambda x: x[0])
        
        stack = []
        
        for robot in robots:
            # If the robot is moving Right, it just goes on the stack waiting for potential 'L' robots
            if robot[2] == 'R':
                stack.append(robot)
            else:
                # Robot is moving Left. Resolve collisions with any 'R' robots on the stack
                while stack and stack[-1][2] == 'R':
                    top_robot = stack[-1]
                    
                    if top_robot[1] > robot[1]:
                        # Stack top survives, current robot is destroyed
                        top_robot[1] -= 1
                        robot[1] = 0
                        break
                    elif top_robot[1] < robot[1]:
                        # Current robot survives, stack top is destroyed
                        stack.pop()
                        robot[1] -= 1
                    else:
                        # Both have the same health, both are destroyed
                        stack.pop()
                        robot[1] = 0
                        break
                
                # If the current 'L' robot survived all 'R' robots on the stack, it survives permanently
                if robot[1] > 0:
                    stack.append(robot)
                    
        # Sort the surviving robots by their original index
        stack.sort(key=lambda x: x[3])
        
        # Extract and return just the healths
        return [robot[1] for robot in stack]