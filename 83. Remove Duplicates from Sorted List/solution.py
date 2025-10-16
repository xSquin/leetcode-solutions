# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-101)
        node = dummy
        while head:
            if head.val == node.val:
                head = head.next
            else:
                node.next = ListNode(head.val)
                node = node.next
                head = head.next
        return dummy.next
        