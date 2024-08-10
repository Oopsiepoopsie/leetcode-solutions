# [Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/)

*Easy Sliding Window Problem!*


## Cleaner Solution

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res, cnt = 0, 0

        #using sliding window!!!
        for i in range(len(s)):
            if s[i] in vowels:
                cnt += 1
            #here we check the left side character!
            if i >= k and s[i - k] in vowels:
                cnt -= 1
            res = max(res, cnt)

        return res
```
## My Method (Two Pointer)
```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        res = 0

        count = 0
        #left pointer
        left = 0
        #right pointer
        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i - left == k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            
            res = max(res, count)

        return res
```