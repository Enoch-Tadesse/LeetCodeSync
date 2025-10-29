class Solution {
public:
    int smallestNumber(int n) {
        vector<int> nums;
        int curr = 0;
        for (int i = 0; i < 10; i++) {
            curr <<= 1;
            curr |= 1;
            nums.push_back(curr);}
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] >= n) r = mid - 1;
            else l = mid + 1; 
        }
        return nums[l];
    }
};