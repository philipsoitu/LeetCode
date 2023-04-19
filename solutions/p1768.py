class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        shortest_word = min(len(word1), len(word2))
        for i in range(shortest_word):
            ans+=word1[i] + word2[i]
        ans+= word1[shortest_word:] + word2[shortest_word:]
        return ans


print(Solution.mergeAlternately(Solution, "", "123"))
        