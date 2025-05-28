class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.prereq = defaultdict(list)
        for a, b in prerequisites:
            self.prereq[a].append(b)
        self.visited = set()
        for course in range(numCourses):
            if self.dfs(course, set()):
                return False
        return True

# return if there is a loop
    def dfs(self, cur, path: set):
        if cur in self.visited:
            return False
        if cur in path:
            return True
        path.add(cur)
        ends = self.prereq[cur]
        for end in ends:
            if self.dfs(end, path):
                return True
        path.remove(cur)
        self.visited.add(cur)
        return False
        
        
        
        