class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()

# test
string = "HelloWorld"
result = Solution().toLowerCase(string)
print(result)