# **217. Contains Duplicate**

# Question
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.\
\
Difficulty: Easy
<br/>

# Example test cases
1. Input: nums = [1,2,3,1] Output: true
   
2. Input: nums = [1,2,3,4] Output: false
   
3. Input: nums = [1,1,1,3,3,4,3,2,4,2] Output: true

<br/>

# Solution
## Thought process:
1. Convert nums list to a set (set_nums) to remove duplicates
2. Compare length of list and length of set
3. If length of set is shorter than length of list, it means that some elements (duplicates) are removed from the list when converting to set. Return True.
4. Else, length of set is the same as length of list, no duplicated elements are removed when list is converted to set. Return False
<br/><br/>
- Time complexity: O(1)
- Space complexity: O(n)
<br/><br/>

## Code:
```python
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(set_nums) < len(nums):
            return True
        else:
            return False

# test
l = [1, 2, 3, 5, 4, 1]
result = Solution().containsDuplicate(l)
print(result)
```