# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# key = index, value = Node
# 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hashMap = {}
        dummy = ListNode(0)
        dummy.next = head


        curr = dummy
        i = 0 
        
        while curr:
            hashMap[i] = curr
            i += 1
            curr = curr.next

        
        removeIndex = len(hashMap) - n -1

        prev = hashMap[removeIndex]
        prev.next = prev.next.next 
        if removeIndex == 0:
            head = prev.next
    
        return head






