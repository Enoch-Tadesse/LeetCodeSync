typedef vector<int> vi;

class SegmentTree {
    private:
        vi st;
        int n;
        int leftPos(int x) {return (x << 1) + 1;}
        int rightPos(int x) {return (x << 1) + 2;}

        void updateHelper(int p, int idx, int val, int l, int r) {
            if (l == r) {
                st[p] += val;
                return;
            }
            int mid = l + (r - l) / 2;
            if (idx <= mid) updateHelper(leftPos(p), idx, val, l, mid );
            else updateHelper(rightPos(p), idx, val, mid + 1, r);
            st[p] = st[leftPos(p)] + st[rightPos(p)];
        }
        int queryHelper(int p, int l, int r, int L, int R) {
            if (l > R || r < L) return 0;
            if (l >= L && r <= R) return st[p];
            int mid = l + (r - l) / 2;
            int s1 = queryHelper(leftPos(p), l, mid, L, R);
            int s2 = queryHelper(rightPos(p), mid + 1, r, L, R);
            return s1 + s2;
        }
    public:
        SegmentTree(int n) {
            this->n = n;
            st.assign(4 * n, 0);
        }

        void update(int idx, int val) {
            updateHelper(0, idx, val, 0, n - 1);
        }

        int query(int right) {
            return queryHelper(0, 0, n - 1, 0, right);
        }

};

class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        unordered_set<int> unique;
        for (int num: nums) unique.insert(num);
        vector<int> pure;
        pure.assign(unique.begin(), unique.end());
        sort(pure.begin(), pure.end());

        unordered_map<int, int> rank;
        for (int i = 0; i < pure.size(); i++) rank[pure[i]] = i;

        vi ans; SegmentTree *st = new SegmentTree(nums.size());
        for (int i = nums.size() - 1; i > -1; i--) {
            ans.push_back(st->query(rank[nums[i]] - 1));
            st->update(rank[nums[i]], 1);
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};
// if the max number from l and r is smaller than that number, that means r - l + 1 numbers are smaller than it