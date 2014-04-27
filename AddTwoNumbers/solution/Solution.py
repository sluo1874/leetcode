# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        resList = ListNode(0)
        cursor = resList
        
        add = 0
        
        while True:
            if l1 and l2:
                sumation = l1.val + l2.val + add
                add = 0
                if sumation > 9:
                    add = 1
                    sumation -= 10
                cursor.next = ListNode(sumation)
                cursor = cursor.next
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sumation = l1.val + add
                add = 0
                if sumation > 9:
                    add = 1
                    sumation -= 10
                cursor.next = ListNode(sumation)
                cursor = cursor.next
                l1 = l1.next
            elif l2:
                sumation = l2.val + add
                add = 0
                if sumation > 9:
                    add = 1
                    sumation -= 10
                cursor.next = ListNode(sumation)
                cursor = cursor.next
                l2 = l2.next
            else:
                break
        if add == 1:
            cursor.next = ListNode(1)
        return resList.next
    
    
if __name__ == "__main__":
    so = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print so.addTwoNumbers(l1, l2)
                
                
            