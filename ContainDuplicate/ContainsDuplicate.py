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