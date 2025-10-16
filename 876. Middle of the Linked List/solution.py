# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def check_length(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        middle = 0
        count = 0
        length = check_length(head)

        if length % 2 == 0:
            middle = length / 2 
        else:
            middle = int(length / 2)

        while head:
            count += 1
            if length == 1:
                return head
            elif middle == count:
                return head.next
            head = head.next
        
        