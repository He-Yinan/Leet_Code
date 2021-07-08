# **187.Repeated DNA Sequences**

# Question
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

- For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
<br/>

Difficulty: Medium
<br/>

---
# Example test cases
1. Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"] 
<br/>
   
2. Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
<br/>

---
# Constraints
- 1 <= s.length <= 105
- s[i] is either 'A', 'C', 'G', or 'T'.
<br/>

---
# Solution
## Thought process:
1. If length of string is less than 10, there is no substrings, return empty list
2. Use a sliding window of size 10 to go through the string
3. If the substring exists in past sequence set, add the substring to repeated sequence.
4. If the substring does not exist in past sequence set, it means the substring has not been encountered before, add the substring to past sequence set.

Variables:
- repeated_seq: stores the set of strings that have been encountered before.
- past_substring: stores the unique strings that are encountered.
- l_ptr: points to the left boundary of the window.
<br/>

- Time complexity: O(n) (string slicing takes O(length of slice) = O(10))
- Space complexity: O(n)
<br/>

## Code:
```python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if(len(s) <= 10):
            return []

        repeated_seq = set()
        l_ptr = 0
        past_substring = set()

        while l_ptr < len(s)-9:
            substring = s[l_ptr:l_ptr+10]
            if substring in past_substring:
                # substring was encountered before, add substring to repeated string
                repeated_seq.add(substring)
            else:
                # substring has never been encountered before, add substring to past substring
                past_substring.add(substring)
            l_ptr += 1

        return repeated_seq
```