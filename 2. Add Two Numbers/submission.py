# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        left, deep = 0, 0
        while l1 != None:
            left += l1.val * 10 ** deep
            deep += 1
            l1 = l1.next
        
        right, deep = 0, 0
        while l2 != None:
            right += l2.val * 10 ** deep
            deep += 1
            l2 = l2.next
        
        result = left + right
        value = result % 10
        l = ListNode(value)
        head = l
        
        while result / 10 > 0 and result >= 10:
            result = result // 10
            value = result % 10
            temp = ListNode(value)
            l.next = temp
            l = l.next
        return head
        
