# **58. Length of Last Word**

# Question
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.\
\
Difficulty: Easy

<br/>

# Example test cases
1. Input: s = "Hello World" Output: 5
   
2. Input: s = " " Output: 0

<br/>

# Constraints
- 1 <= s.length <= 104
- s consists of only English letters and spaces ' '

<br/>

# Solution
## Thought process:
1. Use split() method to split the string by ' ' and return a list, assign this list to l.
2. Access last element of l by indexing -1. 
3. Get and return length using len() method.

<br/>

## Code:
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split string into a list l, default separator is whitespace
        l = s.split()

        # return 0 if list is empty
        if len(l) == 0:
            return 0

        return len(l[-1])

#test
string = "Hello world"
result = Solution().lengthOfLastWord(string)
print(result)
```