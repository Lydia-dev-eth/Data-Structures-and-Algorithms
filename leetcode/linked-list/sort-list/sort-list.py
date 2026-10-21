class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # A list with zero or one node is already sorted.
        if not head or not head.next:
            return head

        # Find the middle of the linked list.
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves.
        mid = slow.next
        slow.next = None

        # Recursively sort both halves.
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves.
        return self.merge(left, right)

    def merge(
        self,
        left: Optional[ListNode],
        right: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy node to simplify merging.
        dummy = ListNode()
        tail = dummy

        # Compare the front nodes and attach the smaller one.
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        # Attach the remaining nodes.
        tail.next = left if left else right

        return dummy.next


# Time Complexity: O(n log n)
# Space Complexity: O(log n) — recursive call stack
 
