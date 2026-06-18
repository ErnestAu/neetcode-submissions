# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False



        # hashSet = set()
        # curr = head
        # while curr:
        #     if curr in hashSet:
        #         return True 
        #     hashSet.add(curr)
        #     curr = curr.next

        