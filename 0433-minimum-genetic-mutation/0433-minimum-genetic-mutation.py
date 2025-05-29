class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        q = deque()
        q.append(startGene)
        
        step = 0
        res = 11
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                visited.add(cur)
                if cur == endGene:
                    res = min(res, step)
                for i in self.generateGene(cur):
                    if i in bank and i not in visited:
                        q.append(i)
            step += 1

        
        return res if res <= 10 else -1
    
    def generateGene(self, gene: str) ->List[str]:
        res = []
        choices = ['A', 'C', 'G', 'T']
        gene = list(gene)
        for i in range(len(gene)):
            for c in choices:
                if gene[i]!= c:
                    this = gene[:i] + [c] + gene[i+1:]

                    res.append(''.join(this))
        return res
 