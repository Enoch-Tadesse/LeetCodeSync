class Solution {
public:
    int minCost(string colors, vector<int>& neededTime) {
        long long ans = 0;
        vector<int> stack;
        for (int i = 0; i < colors.size(); i++) {
            char c = colors[i];
            if (stack.size() != 0) {
                int top = stack[stack.size() -1];
                if (colors[top] == c) {
                    if (neededTime[top] < neededTime[i]) {
                        ans += (long long)neededTime[top];
                        stack.pop_back();
                    }else {
                        ans += (long long)neededTime[i];
                        continue;
                    }
                }
            }
            stack.push_back(i);
        }
        return ans;
    }
};