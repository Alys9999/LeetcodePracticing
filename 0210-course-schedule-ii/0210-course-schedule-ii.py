class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.prereq = defaultdict(list)
        self.postorder = []
        for a, b in prerequisites:
            self.prereq[a].append(b)
        self.visited = set()
        for course in range(numCourses):
            if self.dfs(course, set()):
                return []
        return self.postorder

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
        self.postorder.append(cur)
        self.visited.add(cur)
        return False
