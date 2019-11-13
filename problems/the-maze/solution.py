# Problem link: https://leetcode.com/problems/the-maze/
from collections import deque as que
class Solution:
    def hasPath(self, maze, start, destination):
        q = que([])
        # Maze dimensions
        n = len(maze)
        m = len(maze[0])
        dir = ((0,1), (0,-1), (1,0), (-1,0))
        q.append(start)
        while len(q) > 0:
            x, y = q.popleft()
            #Tainting the visited node
            maze[x][y] = 2
            if x == destination[0] and y == destination[1]:
                return True
            for x_inc, y_inc in dir:
                #BFS traversal
                row = x + x_inc
                col = y + y_inc
                #Move in that direction until we hit the wall/obstacle
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x_inc
                    col += y_inc
                row -= x_inc
                col -= y_inc
                #Check if we have not visited this location before
                if maze[row][col] == 0:
                    q.append([row,col])        
        return False
