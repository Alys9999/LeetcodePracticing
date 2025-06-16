class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        l = split(',', preorder)

        def compose(nodes):
            if not nodes:
                return False
            first = nodes.pop(0)
            if first == '#':
                return True
            return compose(nodes) and compose(nodes)
        return compose(l) and len(l) == 0