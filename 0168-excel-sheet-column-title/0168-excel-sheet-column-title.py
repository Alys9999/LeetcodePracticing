class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = deque()
        while columnNumber:
            columnNumber -= 1
            i = chr(columnNumber%26 + 65)
            res.appendleft(i)
            columnNumber = columnNumber // 26 
        return ''.join(res)