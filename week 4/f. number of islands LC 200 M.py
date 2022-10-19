class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length, breadth = len(grid), len(grid[0])
        
        # this funnction when comes across a land co-ordinate, it does a bfs and fills all the connect lands with "v" as in visited
        def fill (i, j):
            if grid[i][j] == "1":
                grid[i][j] = "v"
                
                for x, y in [[-1,0] , [0,1], [1,0], [0,-1]]:
                    if i + x >= 0 and i + x < length and j + y >= 0 and j + y < breadth:
                        fill(i+x, j+y)
        
        count = 0
        # iterating, if we find a land that is not visited yet, we cann the fill() function
        # it marks the respective island visited, so it doesn't gets counted again.
        # we iterate through the matrix, and anytime an unvisited land is seen, count++ is done.
        # As visiting one point of an island marks it completely, we have no chance for repetition.
        for i in range(length):
            for j in range(breadth):
                if grid[i][j] == "1":
                    count += 1
                    fill(i, j)
        
        return count
