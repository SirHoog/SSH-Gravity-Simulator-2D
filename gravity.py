import collections

import numpy as np

class DoubleBuffer:
    def __init__(self, o, n):
        self.old = o
        self.new = n

class GravitySim:
    def __init__(self):
        self.G  = 6.67430e-11  # Gravitational constant

        # Structure of Arrays (SoA)
        # Double buffer of vectors
        self.ps = DoubleBuffer(np.ndarray((0, 2)), np.ndarray((0, 2))) # Positions
        self.vs = DoubleBuffer(np.ndarray((0, 2)), np.ndarray((0, 2))) # Velocities

        self.trailLength = 100 # Ticks
        self.trails = collections.deque(maxlen=self.trailLength) # Buffer of past positions

    def AddBody(self, p):
        self.ps.new = np.append(self.ps.new, p, axis=0)
        self.vs.new = np.append(self.vs.new, np.random.rand(1, 2), axis=0)

        self.ps.old = np.append(self.ps.old, self.ps.new[-1], axis=0)
        self.vs.old = np.append(self.vs.old, self.vs.new[-1], axis=0)

    def Update(self):
        for i in range(len(self.ps.old)):
            p1 = self.ps.old[i]

            for j in range(len(self.ps.old)):
                if i != j:
                    p2 = self.ps.old[j]

                    r = p2 - p1
                    r_norm = np.linalg.norm(r)
                    
                    if r_norm > 0:
                        a = self.G / r_norm**2 # All masses are equal to 1
                        a_vec = a * r / r_norm
                        self.vs.new[i] += a_vec
            
            self.ps.new[i] += self.vs.new[i]
        
        self.trails.append(self.ps.old)

        for i in range(len(self.ps.old)):
            self.vs.old[i] = self.vs.new[i]
            self.ps.old[i] = self.ps.new[i]
        