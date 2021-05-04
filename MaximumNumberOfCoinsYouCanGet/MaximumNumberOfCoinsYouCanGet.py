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