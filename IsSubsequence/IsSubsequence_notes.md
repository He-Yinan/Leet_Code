# **392. Is Subsequence**

# Question

Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).\
\
Difficulty: Easy
<br/>

# Example test cases
1. Input: s = "abc", t = "ahbgdc" Output: true
   
2. Input: s = "axc", t = "ahbgdc" Output: false


<br/>

# Constraints
- 0 <= s.length <= 100
- 0 <= t.length <= 104
- s and t consist only of lowercase English letters.

<br/>

# Solution
## Thought process:
1. Maintain two pointers s_index and t_index. Initialize both to 0 (point to start of the two strings), initialize r to False.
2. Iterate through t. Add 1 to t_index for every iteration.
3. Add 1 to s_index when the current s character pointed at is equal to the t character pointed at.
4. If s character is equal to t character and it is the last s character, set r to True.
<br/><br/>
- Time complexity: O(n)
- Space complexity: O(1)
<br/><br/>

## Code:
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # return true if s is an empty string. (set by question)
        if len(s) == 0:
            return True

        # initialize variables
        s_index = 0
        t_index = 0
        r = False

        # iterate through every character in t
        while t_index < len(t):
            if s[s_index] == t[t_index]:
                # if last character of s is reached and it is found in t, it means all previous characters of s is a subsequence of the previous characters of t
                if s_index == len(s) -1:
                    r = True
                    break
                s_index += 1
            t_index += 1
        return r

# test
s = "abc"
t = "ahbgdc"
result = Solution().isSubsequence(s, t)
print(result)
```