#include <climits>
#include <vector>
using namespace std;

typedef vector<int> vi;
class SegmentTree {
    private:
        vi nums, st;
        int n;
        int left(int x) { return (x << 1) + 1; }
        int right(int x) { return (x << 1) + 2; }
        void build(int p, int l, int r) {
            if (l == r) {
                st[p] = nums[l];
                return;
            }

            int mid = l + (r - l) / 2;
            build(left(p), l, mid);
            build(right(p), mid + 1, r);
            st[p] = st[left(p)] + st[right(p)];
        }

        int queryHelper(int p, int l, int r, int ql, int qr) {
            if (qr < l || ql > r) return 0;
            if (ql <= l && r <= qr) return st[p];
            int mid = l + (r - l) / 2;
            int s1 = queryHelper(left(p), l, mid, ql, qr);
            int s2 = queryHelper(right(p), mid + 1, r, ql, qr);
            return s1 + s2;
        }

        void updateHelper(int p, int idx, int val, int l, int r) {
            if (l == r) {
                st[p] = val;
                return;
            }
            int mid = l + (r - l) / 2;
            if (idx <= mid)
                updateHelper(left(p), idx, val, l, mid);
            else
                updateHelper(right(p), idx, val, mid + 1, r);
            st[p] = st[left(p)] + st[right(p)];
        }

    public:
        SegmentTree(vi nums) {
            this->nums = nums;
            n = nums.size();
            st.assign(4 * n, 0);
            build(0, 0, n - 1);
        }

        int query(int l, int r) { return queryHelper(0, 0, n - 1, l, r); }
        void update(int idx, int val) {
            updateHelper(0, idx, val, 0, n - 1);
            nums[idx] = val;
        }
};


class NumArray {
    SegmentTree *sg;
public:
    NumArray(vector<int>& nums) {
        sg = new SegmentTree(nums);
    }
    
    void update(int index, int val) {
        sg->update(index, val);
    }
    
    int sumRange(int left, int right) {
        return sg->query(left, right);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */