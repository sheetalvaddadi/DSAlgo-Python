import collections
class MatrixBFS:
    def num_islands(self,grid):
        num_of_islands =0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]) =="1":
                    self.bfs(grid,i,j)
                    num_of_islands+=1
        return num_of_islands

    def bfs(self, grid, i,j):
        q = collections.deque()
        q.appendleft((i,j))

        while(q):
            row, col = q.pop()
            if row+1 <len(grid) and grid[row+1][col] =="1":
                grid[row+1][col] = "0"
                q.appendleft((row+1,col))
            if row - 1 >=0 and grid[row - 1][col] == "1":
                grid[row - 1][col] = "0"
                q.appendleft((row - 1, col))
            if col + 1 < len(grid[0]) and grid[row][col+1] == "1":
                grid[row][col+1] = "0"
                q.appendleft((row, col+1))
            if col - 1 >=0 and grid[row][col-1] == "1":
                grid[row][col-1] = "0"
                q.appendleft((row, col-1))


if __name__ =="__main__":
    mb = MatrixBFS()
    print(mb.num_islands([
        ['1','1','0'],
        ['0','0','1'],
        ['1','1','1']
    ]))

