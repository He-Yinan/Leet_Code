# **217. Contains Duplicate**

# Question
There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:\
<br/>
- In each step, you will choose any 3 piles of coins (not necessarily consecutive) of your choice.
- Alice will pick the pile with the maximum number of coins.
- You will pick the next pile with maximum number of coins.
- Your friend Bob will pick the last pile.
- Repeat until there are no more piles of coins.
  
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins which you can have.

<br/>
Difficulty: Medium
<br/><br/>

# Example test cases
1. Input: piles = [2,4,1,2,7,8]<br/>
Output: 9<br/>
Explanation: Choose the triplet (2, 7, 8), Alice pick the pile with 8 coins, you pick the pile with 7 coins and Bob pick the last one.
Choose the triplet (1, 2, 4), Alice pick the pile with 4 coins, you pick the pile with 2 coins and Bob pick the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is **not optimal**.
   
2. Input: piles = [2,4,5]<br/>
Output: 4
   
3. Input: piles = [9,8,7,6,5,1,2,3,4]<br/>
Output: 18

<br/>

# Constraints
- 3 <= piles.length <= 10^5
- piles.length % 3 == 0
- 1 <= piles[i] <= 10^4

<br/>

# Solution
## Thought process:
Maximum number of coins you can have is when you chose the 2nd largest pile, 4th largest pile, 6th largest pile etc. This is because the 1st largest pile, 3rd largest pile, 5th largest pile etc is chosen by alice.

1. Sort pile in reverse order
2. Calculate range of piles (indexes) you should choose from (the largest two third)
3. Choose the piles from the range of piles starting from index 1 to index r-1 with a step of 2.
<br/><br/>
- Time complexity: O(nlogn)
- Space complexity: O(1)
<br/><br/>

## Code:
```python
from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # sort piles from largest to smallest
        piles.sort(reverse = True)
        # range of piles you should choose from. eg. choose from 0 to 5 
        # if there are 9 elements
        r = int(len(piles) / 3) * 2
        max_coins = 0
        for i in range(1, r, 2):
            max_coins += piles[i]
        return max_coins

# test
piles = [2, 4, 1, 2, 7, 8]
result = Solution().maxCoins(piles)
print(result)
```