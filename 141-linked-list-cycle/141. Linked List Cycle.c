/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {

    if(!head){
        return false;
    }

    if(!head->next){
        return false;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head->next;

    while(fast->next && fast->next->next){
        if (slow == fast){
            return true;
        }

        fast = fast->next->next;
        slow = slow->next;
    }

    return false;

}