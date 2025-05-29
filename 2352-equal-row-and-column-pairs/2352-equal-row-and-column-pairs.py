class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        cnt = 0

        grid_rev = []
        for i in range(n):
            a = []
            for j in range(n):
                a.append(grid[j][i])
            grid_rev.append(a)
        
        for i in grid:
            for j in grid_rev:
                if i == j:
                    cnt += 1
        return cnt