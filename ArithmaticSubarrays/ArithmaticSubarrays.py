class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        difference = 0

        # iterate all elements in l and r
        for i in range(0, len(l)):
            status = True
            x = l[i]
            y = r[i]
            subarray = nums[x:y+1]
            # sort subarray
            subarray.sort()
            difference = subarray[1] - subarray[0]
            for k in range(2, len(subarray)):
                # check if subarray is arithmatic, if not arithmatic, change status to False
                if(subarray[k] - subarray[k-1] != difference):
                    status = False
                    break
            output.append(status)
        return output