# [Leetcode 2181. Merge Nodes in Between Zeros](https://leetcode.com/problems/merge-nodes-in-between-zeros/description/)

Easy Linked List medium question...

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #the constraint we have at least three nodes...
        first, curr = head.next, head.next.next

        while curr:
            if curr.val == 0:
                #skip zero, change first ptr
                first.next = curr.next
                first = curr.next
            elif first != curr:
                #skip nodes
                first.val += curr.val
                first.next = curr.next
            #moev to the next one
            curr = curr.next
        
        return head.next
```
