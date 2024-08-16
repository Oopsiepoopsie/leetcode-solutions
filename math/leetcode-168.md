# [Leetcode 168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/)

Basically the math behind ***number representation***

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #for storing the letters
        res = []

        #for the rest digits
        while columnNumber:
            #the key step!!! (Because A-Z is from 1-26 which doesnt make sense for modular arithmetic)
            #701 = 26 * 26^1 + 25 = 'ZY' (we change A-Z to 0-25)
            columnNumber -= 1
            #get the remainder each time
            r = columnNumber % 26
            res.append(chr(65 + r))
            columnNumber = columnNumber // 26

        #reverse and concatenate it
        res.reverse()
        return "".join(res)
```