class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = self.quickSelect(nums, k)
        return nums[index]

    def partition(self, nums, low, high):
        i = low - 1
        pivot = nums[high]

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[high], nums[i+1] = nums[i+1], nums[high]
        return i + 1

    def quickSelect(self, nums, k):
        low, high = 0, len(nums) - 1
        target = len(nums) - k
        p = self.partition(nums, low, high)
        while p != target:
            if target > p:
                low = p + 1
            else:
                high = p - 1
            p = self.partition(nums, low, high)
        return p
