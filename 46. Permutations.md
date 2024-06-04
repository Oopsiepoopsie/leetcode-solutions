## LeetCode 46. Permutations

Backtracking is an effective technique for solving permutation problems by exploring all possible configurations and undoing choices (backtracking) to explore other possibilities. Here's how you can solve the permutation problem using backtracking:

1. **Choose**: Select an element to add to the current permutation.
2. **Explore**: Recursively create permutations with the remaining elements.
3. **Unchoose**: Remove the element (backtrack) and try the next possibility.

Here's the code to solve the permutation problem using backtracking:

```python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            # If the current permutation is complete, add it to the results
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                # Choose
                nums[start], nums[i] = nums[i], nums[start]
                
                # Explore
                backtrack(start + 1)
                
                # Unchoose (backtrack)
                nums[start], nums[i] = nums[i], nums[start]
        
        res = []
        backtrack(0)
        return res
```

### Explanation:

1. **Initialization**:
   - Define the `backtrack` function that will be used to generate permutations.
   - Initialize the result list `res` to store the permutations.

2. **Backtracking Function**:
   - **Base Case**: When `start` reaches the length of `nums`, a complete permutation is formed, so add it to `res`.
   - **Recursive Case**: Iterate over the indices from `start` to the end of the list:
     - Swap the current element (`nums[start]`) with the element at the current index (`nums[i]`) to fix the current element.
     - Recursively call `backtrack` with the next starting index (`start + 1`) to generate permutations of the remaining elements.
     - Swap back to restore the original list configuration (backtrack).

3. **Start Backtracking**:
   - Call the `backtrack` function starting from index `0`.

This approach ensures that all permutations are generated without modifying the original list `nums` permanently, as each recursive call explores a different configuration.
