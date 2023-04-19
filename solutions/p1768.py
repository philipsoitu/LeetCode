class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(i[0]+i[1] for i in zip(word1,word2)) + word1[len(word2):] + word2[len(word1):]
