/*
*  Maximum Subarray
*/

// subproblem - max_sum = max(max_sum[i-1] + nums[i], nums[i])
class Solution {
public:
    int max_sub_arrray(vector<int>& nums) {
        if (nums.size() < 2) {
            return nums[0];
        }
        
        int curr_max = nums[0];
        int max_so_far = nums[0];
        for(int i = 1; i < nums.size(); i++) {
            curr_max = max(nums[i], curr_max + nums[i]);
            max_so_far = max(curr_max, max_so_far);
        }
        
        return max_so_far;
    }
};
