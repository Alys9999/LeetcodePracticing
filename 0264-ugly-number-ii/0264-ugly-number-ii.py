class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 1, 1, 1
        pro2, pro3, pro5 = 1, 1, 1
        res = [0] * (n+1)

        p = 1

        while p < n + 1:
            minV = min(pro2, pro3, pro5)
            res[p] = minV
            p += 1
            if minV == pro2:
                pro2 = 2 * res[p2]
                p2 += 1
            if minV == pro3:
                pro3 = 3*res[p3]
                p3 += 1
            if minV == pro5:
                pro5 = 5*res[p5]
                p5 += 1
        return res[n]