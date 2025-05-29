class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        visited = set()
        visited.add(0)
        while stack:
            cur = stack.pop()
            for i in rooms[cur]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return len(rooms) == len(visited)