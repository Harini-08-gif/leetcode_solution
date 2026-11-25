# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        temp = head

        # Step 1: Count the total number of nodes.
        while temp is not None:
            length += 1
            temp = temp.next

        # Step 2: Find the position before the node to remove.
        position = length - n

        # Step 3: If the head node needs to be removed.
        if position == 0:
            return head.next

        temp = head
        count = 1

        # Step 4: Traverse to the required position.
        while temp is not None:

            if count == position:
                temp.next = temp.next.next
                return head

            count += 1
            temp = temp.next

        return head
