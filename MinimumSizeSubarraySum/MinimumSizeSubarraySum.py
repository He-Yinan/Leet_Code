class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        l = 0
        r = 0
        s = nums[0]
        length = len(nums)

        while l < length and r < length:
            while s >= target:
                if r-l+1 < min_len:
                    min_len = r - l + 1
                if l < r:
                    s -= nums[l]
                    l += 1
                else:
                    return 1
            if r+1 < length:
                r += 1
                s += nums[r]
            else:
                break

        if min_len == float('inf'):
            return 0

        return min_len
