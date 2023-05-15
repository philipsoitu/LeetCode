class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        longest_sequence = 0
        current_sequence = 0
        for i in range(len(s)):
            if s[i] in hm:
                longest_sequence = max(longest_sequence, current_sequence)
                current_sequence = 0
            
            current_sequence+=1
            hm[s[i]] = i
        return max(longest_sequence, current_sequence)


string = "abcabcabc"
print(Solution.lengthOfLongestSubstring(Solution, string))
