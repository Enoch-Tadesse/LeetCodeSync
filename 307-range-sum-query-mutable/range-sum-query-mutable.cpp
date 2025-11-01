typedef vector<int> vi;

class SegmentTree {
    private:
        vi nums, sg;
        int n;
        int left(int x) {return (x << 1) + 1;}
        int right(int x) {return (x << 1) + 2;}
        void build(int p, int l, int r){
            if (l == r) {
                sg[p] = nums[l];
                return;
            }
            int mid = l + (r - l) / 2;
            int le = left(p), ri = right(p);
            build(le, l, mid); build(ri, mid + 1, r);
            sg[p] = sg[le] + sg[ri];
        }
        int queryHelper(int p, int l, int r, int L, int R) {
            if (l > R || r < L) return 0;
            if (L <= l && r <= R) return sg[p];
            int le = left(p), ri = right(p);
            int mid = l + (r - l) / 2;
            int s1 = queryHelper(le, l, mid, L, R);
            int s2 = queryHelper(ri, mid + 1, r, L, R);
            return s1 + s2;            
        }
        void updateHelper(int p, int idx, int val, int l, int r) {
            if (l == r) {
                sg[p] = val;
                return;
            }
            int mid = l + (r - l) / 2;
            if (idx <= mid) updateHelper(left(p), idx, val, l, mid);
            else updateHelper(right(p), idx, val, mid + 1, r);
            sg[p] = sg[left(p)] + sg[right(p)];
        }
    public:
        SegmentTree(vi nums) {
            this->nums = nums;
            n = nums.size();
            sg.assign(4 *n, 0);
            build(0, 0, n - 1);
        }

        int query(int left, int right) {
            return queryHelper(0, 0, n - 1, left, right);
        }

        void update(int index, int val) {
            updateHelper(0, index, val, 0, n - 1);
            nums[index] = val;
        }

};

class NumArray {
public:
    SegmentTree *sg;
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