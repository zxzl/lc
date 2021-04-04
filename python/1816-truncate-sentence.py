class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split()

        return_words = words[:k]

        return " ".join(return_words)
