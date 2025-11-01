/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        ListNode *dummy = new ListNode();
        ListNode *curr = dummy;
        unordered_set<int> toremove;
        for (int num: nums) toremove.insert(num);
        while (head) {
            if (toremove.find(head->val) == toremove.end()) {
                curr->next = head;
                curr = curr->next;
            }
            head = head->next;
        }
        curr->next = nullptr;
        return dummy->next;
    }
};