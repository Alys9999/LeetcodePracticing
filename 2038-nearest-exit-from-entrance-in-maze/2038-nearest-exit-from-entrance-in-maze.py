class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        q = deque()
        visited = set()
        visited.add((entrance[0], entrance[1]))
        q.append([entrance[0], entrance[1],0])
        row = len(maze)
        col = len(maze[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while q:
            r,c,step = q.popleft()
            if( r!= entrance[0] or c != entrance[1]) and (r in [0, row-1] or c in [0, col-1]):
                return step
            for direction in directions:
                next_row = r+direction[0]
                next_col = c+direction[1]
                if 0<=next_row and next_row<row and 0<=next_col and next_col<col: 
                    if (next_row, next_col) not in visited and maze[next_row][next_col] == ".":
                        visited.add((next_row, next_col))
                        q.append((next_row, next_col, step+1))

        return -1