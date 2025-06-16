class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        cur = 1
        preorder = split(',', preorder)
        for node in preorder:
            if node == '#':
                cur -= 1
                if cur < 0:
                    return False
            else: 
                cur -= 1
                if cur < 0:
                    return False
                cur += 2
            
        return cur == 0
