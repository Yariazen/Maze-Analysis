from abc import ABC, abstractmethod

class Maze(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def algorithm(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    def size(self):
        return self.size

    def newSize(self, newSize):
        self.size = newSize