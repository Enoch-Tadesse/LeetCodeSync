class SegmentTree {
public:
    vector<int> nums;
    int n;
    vector<int> seg;

    SegmentTree(vector<int>& nums) {
        this->nums = nums;
        this->n = nums.size();
        seg.assign(4 * n, INT_MAX);
        build(0, 0, n - 1);
    }

    void build(int pos, int l, int r) {
        if (l == r) {
            seg[pos] = nums[l];
            return;
        }
        int mid = (l + r) >> 1;
        build((pos << 1) + 1, l, mid);
        build((pos << 1) + 2, mid + 1, r);
        seg[pos] = min(seg[(pos << 1) + 1], seg[(pos << 1) + 2]);
    }

    int query(int l, int r) {
        return queryHelper(0, 0, n - 1, l, r);
    }

    int queryHelper(int pos, int l, int r, int L, int R) {
        if (l > R || r < L) return INT_MAX;
        if (l >= L && r <= R) return seg[pos];
        int mid = (l + r) >> 1;
        int cand1 = queryHelper((pos << 1) + 1, l, mid, L, R);
        int cand2 = queryHelper((pos << 1) + 2, mid + 1, r, L, R);
        return min(cand1, cand2);
    }
};

class Solution {
public:
    int minOperations(vector<int>& nums) {
        SegmentTree seg(nums);
        unordered_map<int, vector<int>> idx;
        for (int i = 0; i < nums.size(); i++) {
            idx[nums[i]].push_back(i);
        }

        function<int(int,int)> divide = [&](int l, int r) {
            if (l > r) return 0;
            int _min = seg.query(l, r);
            int output = (_min != 0);
            auto& indices = idx[_min];
            auto start = lower_bound(indices.begin(), indices.end(), l) - indices.begin();
            auto end = upper_bound(indices.begin(), indices.end(), r) - indices.begin();
            int last = l;
            for (int k = start; k < end; k++) {
                int i = indices[k];
                if (i > last) output += divide(last, i - 1);
                last = i + 1;
            }
            if (last <= r) output += divide(last, r);
            return output;
        };

        return divide(0, nums.size() - 1);
    }
};
