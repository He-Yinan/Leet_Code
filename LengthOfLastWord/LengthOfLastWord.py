class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split string into a list l, default separator is whitespace
        l = s.split()

        # return 0 if list is empty
        if len(l) == 0:
            return 0

        return len(l[-1])

# test
string = "Hello world"
result = Solution().lengthOfLastWord(string)
print(result)