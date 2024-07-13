# [Leetcode 67. Add Binary](https://leetcode.com/problems/add-binary/description/)

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        ptr_a, ptr_b = len(a) - 1, len(b) - 1

        #the last condition 'carry' is used to check for the last carry!
        while ptr_a >= 0 or ptr_b >= 0 or carry:
            if ptr_a >= 0: 
                carry += int(a[ptr_a])
                ptr_a -= 1
            if ptr_b >= 0: 
                carry += int(b[ptr_b])
                ptr_b -= 1
            #SMART!
            res.append(str(carry % 2))
            #SO SMART!
            carry = carry // 2
            #same as
            # carry = 1 if carry > 1 else 0 

        return ''.join(reversed(res))



#Sneaky solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int('0b'+a, 2) + int('0b'+b, 2))[2:]

```