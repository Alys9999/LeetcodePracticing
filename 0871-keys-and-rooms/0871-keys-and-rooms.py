class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = set()
        q = deque()
        q.append(0)
        while q:
            roomNum = q.popleft()
            if roomNum in visited:
                continue
            visited.add(roomNum)
            for i in rooms[roomNum]:
                q.append(i)


        return len(visited) == n