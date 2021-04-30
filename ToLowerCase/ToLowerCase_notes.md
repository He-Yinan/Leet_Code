# **709. To Lower Case**


# Question
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.\
\
Difficulty: Easy

<br/>

# Example test cases
1. Input: "Hello" Output: "hello"

2. Input: "here" Output: "here"

3. Input: "LOVELY" Output: "lovely"

<br/>

# Solution

## Thought process:
Use lower() method to convert all uppercase characters in a string to lowercase and return it. <br/><br/>

## Code:
```python
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

# test
string = "HelloWorld"
result = Solution().toLowerCase("Hello")
print(result)
```







