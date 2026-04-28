class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> nums;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                nums.push_back(grid[i][j]);
            }
        }
        sort(nums.begin(), nums.end());
        int n_total = nums.size();
        int target = nums[n_total / 2];
        int remainder = nums[0] % x;
        int operations = 0;
        for (int num : nums) {
            if (num % x != remainder) {
                return -1;
            }
            operations += abs(num - target) / x;
        }
        return operations;
    }
};