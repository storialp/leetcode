class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        longest_substring = []
        for i in range(len(s)):
            try:
                dup_index = longest_substring.index(s[i])   
                del longest_substring[:dup_index + 1]
            except:
                pass
            longest_substring.append(s[i])
            max_len = max(max_len, len(longest_substring))
        return max_len