class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        c = 0
        n = len(word1)
        m = len(word2)
        mini = min(n, m)

        while c < mini:
            res.append(word1[c])
            res.append(word2[c])
            c += 1
        if n > m :
            res.append(word1[c:])
        elif m > n:
            res.append(word2[c:])
        return "".join(res)