class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        robots.sort() 
        
        stack = []
        
        for robot in robots:
            if robot[2] == 'R':
                stack.append(robot)
            else:
                while stack and stack[-1][2] == 'R' and robot[1] > 0:
                    top_r = stack[-1]
                    
                    if top_r[1] > robot[1]:
                        top_r[1] -= 1
                        robot[1] = 0
                    elif top_r[1] < robot[1]:
                        robot[1] -= 1
                        stack.pop()
                    else:
                        robot[1] = 0
                        stack.pop()   
                        
                if robot[1] > 0:
                    stack.append(robot)
                    
        stack.sort(key=lambda x: x[3])
        return [robot[1] for robot in stack]