```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    # Approach 1: Recursion
    def reverseList_recursive(self, head):
        if not head or not head.next:
            return head

        new_head = self.reverseList_recursive(head.next)

        head.next.next = head
        head.next = None

        return new_head


    # Approach 2: Iteration
    def reverseList_iterative(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev, current = current, next_node

        return prev


# Approach 1 — Recursion
# Time Complexity: O(n)
# Space Complexity: O(n)


# Approach 2 — Iteration
# Time Complexity: O(n)
# Space Complexity: O(1)
```
