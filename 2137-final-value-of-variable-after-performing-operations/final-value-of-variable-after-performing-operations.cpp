class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int ans = 0;
        for (auto &op: operations) {
            if (op[0] == '-' or op[2] == '-') ans--;
            else ans++;
        }
        return ans;
    }
};