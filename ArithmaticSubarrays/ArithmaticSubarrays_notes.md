# **1630. Arithmetic Subarrays**

# Question

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.<br/>

For example, these are arithmetic sequences:<br/>
1, 3, 5, 7, 9<br/>
7, 7, 7, 7<br/>
3, -1, -5, -9<br/><br/>
The following sequence is not arithmetic:<br/>
1, 1, 2, 5, 7<br/><br/>
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.
\
\
Difficulty: Medium
<br/>

# Example test cases
1. Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]<br/>
   Output: [true,false,true]<br/>
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
   
2. Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]<br/>
   Output: [false,true,false,false,true,true]


<br/>

# Constraints
- n == nums.length
- m == l.length
- m == r.length
- 2 <= n <= 500
- 1 <= m <= 500
- 0 <= l[i] < r[i] < n
- -105 <= nums[i] <= 105

<br/>

# Solution
## Thought process:
1. For each l[i] and r[i], get the subarray.
2. Sort the subarray using python sort(). sort() is an inplace sorting function that is O(nlogn).
3. Calculate the difference between the 1st and 2nd element of the array.
4. Check the rest of the subarray, if there exist a case that subarray[k] - subarray[k-1] != difference, subarray is not arithmatic, modify status to false and break.
5. Append status to the output list. Repeat step 1 to 5 for all elements in l and r.
<br/><br/>
- Time complexity: O(m*nlogn)
- Space complexity: O(m+n)
<br/><br/>

## Code:
```python
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
```