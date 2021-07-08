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
