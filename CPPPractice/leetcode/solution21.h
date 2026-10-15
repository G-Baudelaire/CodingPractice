//
// Created by Germain Jones on 30/07/2025.
//

#ifndef SOLUTION21_H
#define SOLUTION21_H

struct ListNode {
  int val;
  ListNode *next;

  ListNode() : val(0), next(nullptr) {
  }

  ListNode(int x) : val(x), next(nullptr) {
  }

  ListNode(int x, ListNode *next) : val(x), next(next) {
  }
};

class Solution21 {
public:
  ListNode *mergeTwoLists(ListNode *list1, ListNode *list2) {
    ListNode *dummy = new ListNode();
    ListNode *head = dummy;

    while (list1 && list2) {
      if (list1->val < list2->val) {
        head->next = new ListNode(list1->val);
        list1 = list1->next;
      } else {
        head->next = new ListNode(list2->val);
        list2 = list2->next;
      }
      head = head->next;
    }

    if (!list1 && !list2) return nullptr;
    ListNode *remainder = (list1 == nullptr) ? list2 : list1;
    head->next = remainder;
    return dummy->next;
  }
};
#endif //SOLUTION21_H