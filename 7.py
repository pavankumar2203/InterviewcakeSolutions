import sys

class Temperature:

    def __init__(self):
        self.occ = [0 for x in range(0,111)]
        self.total = 0
        self.sum = 0
        self.max = sys.maxsize
        self.min = -sys.maxsize - 1
        self.mean = None
        self.mode = None

    def insert(self, temp):
        self.occ[temp] += 1
        self.total += 1
        self.sum += temp
        self.max = max(self.max, temp)
        self.min = min(self.max, temp)
        self.mean = self.sum/self.total
        self.mode = [x for x in self.occ if max(occ) == x][0]
