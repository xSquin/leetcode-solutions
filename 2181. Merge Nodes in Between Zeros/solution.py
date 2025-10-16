# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = 0
        dummy = ListNode(0)
        node = dummy
        while head:
            if(head.val == 0 and res != 0):
                node.next = ListNode(res)
                node = node.next
                res = 0
            else:
                res += head.val
            head = head.next
        return dummy.next
        
        