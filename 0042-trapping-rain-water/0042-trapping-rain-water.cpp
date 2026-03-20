#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
            if (height.empty()) return 0;

                    int left = 0;
                            int right = height.size() - 1;
                                    int left_max = 0;
                                            int right_max = 0;
                                                    int water_trapped = 0;

                                                            while (left < right) {
                                                                        // We always process the side with the shorter height 
                                                                                    // because that side is the "bottleneck" for trapping water.
                                                                                                if (height[left] < height[right]) {
                                                                                                                if (height[left] >= left_max) {
                                                                                                                                    left_max = height[left];
                                                                                                                                                    } else {
                                                                                                                                                                        water_trapped += (left_max - height[left]);
                                                                                                                                                                                        }
                                                                                                                                                                                                        left++;
                                                                                                                                                                                                                    } else {
                                                                                                                                                                                                                                    if (height[right] >= right_max) {
                                                                                                                                                                                                                                                        right_max = height[right];
                                                                                                                                                                                                                                                                        } else {
                                                                                                                                                                                                                                                                                            water_trapped += (right_max - height[right]);
                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                            right--;
                                                                                                                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                                                                                                                }

                                                                                                                                                                                                                                                                                                                                                        return water_trapped;
                                                                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                                                            };
                                                                                                                                                                                                                                                                                                                                                            