class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        BFS遍历
        """
        queue = []
        n = len(grid)
        # 将陆地格子1添加到queue中
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append([i, j])

        # 如果格子里只有陆地或者海洋返回 -1
        if len(queue) == 0 or len(queue) == n * n:
            return -1
        # 移动距离
        moves = [[-1,0], [1,0], [0,1], [0,-1]]

        distance = -1
        while queue:
            distance += 1
            count = len(queue)
            for i in range(count):
                cur = queue.pop(0)
                for move in moves:
                    c = cur[0] + move[0]
                    r = cur[1] + move[1]
                    if c >= 0 and c < n and r >= 0 and r < n and grid[c][r] == 0:
                        grid[c][r] = 2
                        queue.append([c, r])
        return distance
