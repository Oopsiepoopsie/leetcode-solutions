# [Leetcode 2807. Insert Greatest Common Divisors in Linked List](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/)

Remeber ***Euclidian Algorithm*** to calculate the *grestest common divisor (GCD)*

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #constraint we have at least one node
        prev, curr = head, head.next

        #euclidian algorithm for GCD!!!
        def euclidian(a, b):
            if b == 0: 
                return a
            return euclidian(b, a % b)

        while curr:
            node = ListNode(euclidian(prev.val, curr.val))
            prev.next = node
            node.next = curr
            prev = curr
            curr = curr.next
        
        return head
```