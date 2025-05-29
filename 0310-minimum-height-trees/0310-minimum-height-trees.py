class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # try every node as root
        # in every try, use the final step num as key to record the root
        # use bfs to expand to cover all the nodes
        if n == 1: return [0]
        neighbours = defaultdict(set)
        for e in edges:
            neighbours[e[0]].add(e[1])
            neighbours[e[1]].add(e[0])
        q = deque()
        for i in range(n):
            if len(neighbours[i]) == 1:
                q.append(i)
        nodeCount = n
        while nodeCount > 2:
            size = len(q)
            nodeCount -= size
            for _ in range(size):
                cur = q.popleft()
                for n in neighbours[cur]:
                    neighbours[n].remove(cur)
                    if len(neighbours[n]) == 1:
                        q.append(n)
                
        return list(q)




        # l = defaultdict(list)
        # for r in range(n):
        #     q = deque()
        #     q.append(r)
        #     visited = set()
        #     visited.add(r)
        #     step = 0
        #     while q:
        #         for i in range(len(q)):
        #             cur = q.popleft()
        #             for n in neighbours[cur]:
        #                 if n not in visited:
        #                     visited.add(n)
        #                     q.append(n)
        #         step += 1
        #     l[step].append(r)
        # mini = min(l.keys())
        # return l[mini]
