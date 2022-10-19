class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length, breadth = len(grid), len(grid[0])
        infection_points = []
        # list the coordingates of all rotten oranges
        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == 2:
                    infection_points.append([i,j])
        timer = 0
        # while there are new set of rotten oranges, find their immediate neighbors and mark them rotten
        while(infection_points):
            # print(infection_points)
            temp = []
            
            for i, j in infection_points:
                for x, y in [[-1,0], [1,0], [0,-1], [0,1]]:
                    if 0 <= i + x < length and 0 <= j + y < breadth:
                        # print(length,breadth, i + x, j + y,grid[i + x][j + y])
                        if grid[i + x][j + y] == 1:
                            grid[i + x][j + y] = 2
                            # append new rotten orange coordinates to temp
                            temp.append([i + x, j + y])
            # replace the old set of rotten oranges with that of the "fresh" rots
            infection_points = temp
            # increase timer if there is a new set of oranges to iterate over
            if temp: 
                timer += 1
            
        # check for any leftover fresh oranges. return False, if found.
        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == 1:
                    return -1
        return timer 
