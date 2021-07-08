# **3. Longest Substring Without Repeating Characters**

# Question

Given a string s, find the length of the longest substring without repeating characters.<br/>
Difficulty: Medium

---

# Example test cases
1. Input: s = "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.<br/><br/>


2. Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.<br/><br/>

3. Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring. <br/><br/>

4. Input: s = ""
Output: 0

---

# Constraints
- 0 <= s.length <= 5 * 104
- s consists of English letters, digits, symbols and spaces.

---

# Solution
## Thought process:
1. If string is empty, return 0.
2. If string only has one character, return 1.
3. Since the string left is not empty, the max_length is at least 1.
4. Move right pointer across the string and check each time if there is duplicate in between left and right pointer.
5. If there is duplicate, move the left pointer to the right.
6. If there is no duplicate, keep the left pointer and check if the substring has a length longer than max_length.

<br/>

- Time complexity: O(n^2) where n is the length of the string (set(s) is O(n)) <br/>
- Space complexity: O(1)
<br/>

## Code:
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        if length == 1:
            return 1
        
        l_ptr = 0
        r_ptr = 1
        max_length = 1
        
        while r_ptr < length:
            temp_s = s[l_ptr: r_ptr+1]
            # if duplicate exists in substring
            if len(temp_s) > len(set(temp_s)):
                l_ptr += 1
            # if length of substring is longer than max_length
            elif len(temp_s) > max_length:
                max_length = len(temp_s)
            
            r_ptr += 1 
        return max_length
```