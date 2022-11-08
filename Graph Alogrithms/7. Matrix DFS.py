class MatrixDFS:
    def num_islands(self, grid):
        num_of_islands =0
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if(grid[i][j] =="1"):
                    self.dfs(grid,i,j)
                    num_of_islands+=1
        return num_of_islands

    def dfs(self, grid,row,col):
        grid[row][col] = "0"
        if row+1 < len(grid) and grid[row+1][col]=="1":
           self.dfs(grid,row+1,col)
        if row-1 >=0 and grid[row-1][col]=="1":
           print(grid)
           self.dfs(grid,row-1,col)
        if col + 1 < len(grid[0]) and grid[row][col+1] == "1":
            print(grid)
            self.dfs(grid, row, col+1)
        if col- 1 >=0 and grid[row][col-1] == "1":

            self.dfs(grid, row, col-1)

if __name__ =="__main__":
    m = MatrixDFS()
    print(m.num_islands([
        ['1','1','0'],
        ['0','1','1'],
        ['0','1','0']
    ]))
