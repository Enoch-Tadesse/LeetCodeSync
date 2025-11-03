class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        long long ans = 0;
        vector<int> stack = {-1};
        for (int i = 0; i < colors.size(); i++) {
            char c = colors[i];
            if (stack[0] != -1) {
                int top = stack[0];
                if (colors[top] == c) {
                    if (neededTime[top] < neededTime[i]) {
                        ans += (long long)neededTime[top];
                    }else {
                        ans += (long long)neededTime[i];
                        continue;
                    }
                }
            }
            stack[0] = i;
        }
        return ans;
    }
};