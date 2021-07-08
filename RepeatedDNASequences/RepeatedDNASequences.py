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
