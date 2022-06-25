from maze import Maze
import utility as util
import random as rd
import numpy as np


class Eller(Maze):
    class Cell:
        def __init__(self):
            self.set = []
            self.hasRightWall = False
            self.hasTopWall = False

    def initSets(self, cells, sets):
        for cell in cells:
            if(len(cell.set) == 0):
                cell.set.append(cell)
                sets.append(cell.set)

    def joinRight(self, cells):
        for i in range(len(cells)-1):
            if(bool(rd.getrandbits(1)) or (cells[i].set == cells[i+1].set)):
                cells[i].hasRightWall = True
            else:
                cells[i+1].set.remove(cells[i+1])
                cells[i].set.append(cells[i+1])
                cells[i+1].set = cells[i].set
        cells[len(cells)-1].hasRightWall = True

    def joinTop(self, sets):
        for set in sets:
            if(len(set) > 0):
                for cell in set:
                    walls = 1
                    if((walls < len(set)) and bool(rd.getrandbits(1))):
                        cell.hasTopWall = True
                        walls += 1
            else:
                sets.remove(set)

    def initNext(self, cells):
        for cell in cells:
            cell.hasRightWall = False
            if(cell.hasTopWall):
                cell.set.remove(cell)
                cell.set = []
                cell.hasTopWall = False

    def toMaze(self, states, maze, cells, y):
        for x in range(len(cells)):
            maze[y*2+2][x*2+2] = 1
            if(cells[x].hasRightWall):
                maze[y*2+1][x*2+2] = 1
            if(cells[x].hasTopWall):
                maze[y*2+2][x*2+1] = 1
        states.append(np.copy(maze))

    def algorithm(self):
        size = self.size

        cells = []
        sets = []

        states = []

        maze = np.zeros((size[0]*2+1)*(size[1]*2+1)
                        ).reshape(size[1]*2+1, size[0]*2+1)
        maze[0] = 1
        maze[:, 0] = 1

        for i in range(size[1]):
            if (i == 0):
                for j in range(size[0]):
                    cells.append(self.Cell())
            self.initSets(cells, sets)
            if (i == size[1]-1):
                for j in range(size[0]):
                    cells[j].hasTopWall = True
                    if (j == size[0]-1):
                        cells[j].hasRightWall = True
                    elif (cells[j].set == cells[j+1].set):
                        cells[j].hasRightWall = True
                self.toMaze(states, maze, cells, i)
                continue
            for j in range(size[0]-1):
                if(cells[j].set == cells[j+1].set):
                    cells[j].hasRightWall = True
            self.joinRight(cells)
            self.joinTop(sets)
            self.toMaze(states, maze, cells, i)
            self.initNext(cells)
        return maze, states

    def draw(self):
        size = self.size
        maze, states = self.algorithm()

        util.drawState(maze)
        util.animateStates(states, "BinaryTree")
