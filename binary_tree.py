from maze import Maze
import utility as util
import random as rd
import numpy as np

class Binary_Tree(Maze):
    def update_bt(self, x, y, maze, states):
        size = self.size
        maze[y*2+1][x*2+1] = 0
        if ((y == size[1]-1) and (x == size[0]-1)):
            pass
        elif ((x != size[0]-1) and bool(rd.getrandbits(1)) or (y == size[1]-1) and (x != size[0]-1)):
            maze[y*2+1][x*2+2] = 0
        else:
            maze[y*2+2][x*2+1] = 0
        states.append(np.copy(maze))

    def algorithm(self, size):
        maze = np.ones((size[0]*2+1)*(size[1]*2+1)
                   ).reshape(size[1]*2+1, size[0]*2+1)
        states = []
        for i in range(size[1]):
            for j in range(size[0]):
                self.update_bt(j, i, maze, states)
        return maze, states

    def draw(self):
        size = [25, 25]
        maze, states = self.algorithm(size)

        util.drawState(maze)
        util.animateStates(states, "BinaryTree")