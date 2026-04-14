class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()

        factory_slots = []

        for pos , limit in factory:
            factory_slots.extend([pos] * limit) 

        memo = {}

        def find_min_distance(robot_idx, slot_idx):
            if robot_idx == len(robot):
                return 0 

            if slot_idx == len(factory_slots):
                return float('inf')

            if (robot_idx, slot_idx) in memo:
                return memo[(robot_idx, slot_idx)]

            distance = abs(robot[robot_idx] - factory_slots[slot_idx])

            cost_if_assigned = distance + find_min_distance(robot_idx + 1, slot_idx + 1)

            cost_if_skipped = find_min_distance(robot_idx,slot_idx + 1)

            best_choice = min(cost_if_assigned,
                                  cost_if_skipped)
            memo[(robot_idx, slot_idx)] = best_choice

            return best_choice

        return find_min_distance(0, 0)