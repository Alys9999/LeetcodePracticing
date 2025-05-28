class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.end = len(graph)-1
        self.res = []
        self.dfs(0, list())
        return self.res
    
    def dfs(self, cur, path):
        path.append(cur)
        if cur == self.end:
            self.res.append(path.copy())
        for i in self.graph[cur]:
            self.dfs(i, path)
        path.pop(-1)
