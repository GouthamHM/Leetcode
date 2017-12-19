# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)  # Create a root ListNode to keep track of the digits and n to iterate
        carry = 0
        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            carry, val = divmod(val1 + val2 + carry, 10)
            n.next = n = ListNode(val)  # Chain assignment n.next =  ListNode(val)  then n = n.next so n.next after this step will be None

        return root.next