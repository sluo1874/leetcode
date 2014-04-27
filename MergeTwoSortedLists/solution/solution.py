'''
Created on 2014-4-4

@author: luosai
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if not l2 and not l1:
            return None
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        cursor = head
        while True:
            if l1 and l2:
                if l1.val > l2.val:
                    cursor.next = l2
                    l2 = l2.next
                else:
                    cursor.next = l1
                    l1 = l1.next
                cursor = cursor.next
            elif l1:
                cursor.next = l1
                break
            else:
                cursor.next = l2
                break
        return head
    
    
if __name__ == '__main__':
    l1 = ListNode(2)
    l2 = ListNode(1)
    so = Solution()
    res = so.mergeTwoLists(l1, l2)
    print res