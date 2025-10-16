# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        node = dummy
        while head:
            if head.val != val:
                node.next = ListNode(head.val)
                node = node.next
            head = head.next
        return dummy.next
        