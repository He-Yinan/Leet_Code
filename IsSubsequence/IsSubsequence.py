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