from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid):
        visited = set()
        rows, cols = len(grid), len(grid[0])

        maxcount = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    ans = self.bfs(grid, i, j, visited, rows, cols)
                    maxcount = max(maxcount, ans)

        return maxcount


    def bfs(self, grid, x, y, visited, rows, cols):
        dq = deque()
        dq.append((x, y))
        visited.add((x, y))

        area = 1   # ✅ start count

        dirs = [(0,-1), (0,1), (1,0), (-1,0)]

        while dq:
            xx, yy = dq.popleft()

            for dx, dy in dirs:
                nx, ny = xx + dx, yy + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    if grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        dq.append((nx, ny))
                        area += 1   # ✅ COUNT, not distance

        return area