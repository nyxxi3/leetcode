from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        dist = [[-1 for _ in range(c)] for _ in range(r)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < r and 0 <= nc < c and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[row][col] + 1
                    q.append((nr, nc))

        return dist
