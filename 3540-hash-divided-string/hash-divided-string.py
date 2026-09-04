class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result = []
        n = len(s)
        for i in range(0, n, k):
            sub = s[i:i+k]
            total = sum(ord(c) - ord('a') for c in sub)
            hashed = total % 26
            result.append(chr(ord('a') + hashed))
        return "".join(result)
