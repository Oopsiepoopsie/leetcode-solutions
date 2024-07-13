# [Leetcode 69. Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        #we explore all integers and use binary search to reduce search space
        #(since integers have "sorted" property!!)

        #edge cases
        if x < 2: return x

        #when x >= 2, we can set r to x // 2!!!
        l, r = 0, x // 2

        while l <= r:
            #prevent overflow!!!
            m = l + (r - l) // 2
            if m * m == x:
                return m
            elif m * m < x:
                l = m + 1
            else:
                r = m - 1

        #understand why we return r!!! It converges to the closest number
        return r
```
