# [Leetcode 334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/description/)

*Classic Greedy Problem!*

```python
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for x in nums:
            #the key is to check x to be larger than the SECOND value in the sequence!
            if x > second:
                return True
            #we check whether x should be the first value or the second value in the sequence!
            elif x <= first:
                #if smaller than first, than it can be seen as the NEW first value
                first = x
            elif x <= second:
                second = x

        return False
```