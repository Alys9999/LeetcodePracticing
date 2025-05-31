class Solution:
    def countPrimes(self, n: int) -> int:
        l = [True] * n

        for i in range(2, int(n**0.5)+1):
            if l[i]:
                for j in range(i*i, n, i):
                    l[j] = False
        count = 0
        for c in l[2:]:
            if c:
                count += 1
        return count