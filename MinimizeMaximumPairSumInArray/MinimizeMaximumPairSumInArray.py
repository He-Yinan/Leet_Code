class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        def merge(arr, l, mid, r):
            arr1 = arr[l:mid+1]
            arr2 = arr[mid+1:r+1]

            arr1_len = len(arr1)
            arr2_len = len(arr2)

            ptr1 = 0
            ptr2 = 0

            while ptr1 < arr1_len and ptr2 < arr2_len:
                if arr1[ptr1] < arr2[ptr2]:
                    arr[l] = arr1[ptr1]
                    ptr1 += 1
                elif arr1[ptr1] > arr2[ptr2]:
                    arr[l] = arr2[ptr2]
                    ptr2 += 1
                else:
                    arr[l] = arr1[ptr1]
                    ptr1 += 1
                    l += 1
                    arr[l] = arr2[ptr2]
                    ptr2 += 1
                l += 1

            while ptr1 < arr1_len:
                arr[l] = arr1[ptr1]
                l += 1
                ptr1 += 1

            while ptr2 < arr2_len:
                arr[l] = arr2[ptr2]
                l += 1
                ptr2 += 1

        def mergeSort(arr, l, r):
            if l < r:
                mid = (l+r)//2
                mergeSort(arr, l, mid)
                mergeSort(arr, mid+1, r)
                merge(arr, l, mid, r)
        # do a merge sort
        mergeSort(nums, 0, len(nums)-1)
        l = 0
        r = len(nums) - 1
        max_sum = nums[l] + nums[r]

        # sum all max and min of subarray
        while l < r:
            if nums[l] + nums[r] > max_sum:
                max_sum = nums[l] + nums[r]
            l += 1
            r -= 1

        return max_sum
