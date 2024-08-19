# [Leetcode 258. Add Digits](https://leetcode.com/problems/add-digits/description/)

## Method 1 (Number Theory)
The *best method* that is based on number thoery called [digital root (also repeated digital sum)](https://en.wikipedia.org/wiki/Digital_root)

```python
class Solution:
    def addDigits(self, num: int) -> int:
        '''O(1) method explanation, super smart!!!
        Also simple idea why digital root equals to mod 9 if we've got an ABCD number
        ABCD = 1000A+100B+10*C+D = (A + B + C + D) + 9 * (111 * A + 11 * B + C)
        this equals (mod 9) to A + B + C + D.

        if (A + B + C + D) is greater than 9, we can reapply the formula again, until we get a remainder 
        less than 10!!!     (it would never be 0 and would only be 1 - 9)
        '''

        if num < 10:
            return num
        
        if num % 9 == 0:
            return 9
        else:
            return num % 9
```


## Method 2 (Iteration)
```python
class Solution:
    def addDigits(self, num: int) -> int:
        
        while num // 10 != 0:
            temp = 0
            while num:
                temp += (num % 10)
                num = num // 10
            num = temp
        
        return num
```

## Method 3 (Recursion)
```python
class Solution:
    def addDigits(self, num: int) -> int:
        #recursive method

        #base case
        if num // 10 == 0:
            return num

        temp = 0
        while num:
            temp += (num % 10)
            num = num // 10
        
        return self.addDigits(temp)
```