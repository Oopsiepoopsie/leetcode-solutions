# [Leetcode 83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #prev pointer and curr pointer
        prev, curr = None, head

        while curr:
            if prev and prev.val == curr.val:
                curr = curr.next
                prev.next = curr
            else:
                #move to the next one
                prev = curr
                curr = curr.next

        return head



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        #another method. just check curr and curr.next
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res
```
