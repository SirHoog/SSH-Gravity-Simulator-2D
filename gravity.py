import numpy as np

class GravitySim:
    def __init__(self):
        self.G  = 6.67430e-11  # Gravitational constant
        self.ps = np.array([]) # Positions
        self.vs = np.array([]) # Velocities
        self.ms = np.array([]) # Masses

    def AddBody(self, ps, vs, ms):
        self.ps = np.append(self.ps, ps)
        self.vs = np.append(self.vs, vs)
        self.ms = np.append(self.ms, ms)
    def AddBodies(self, ps, vs, ms):
        for p, v, m in zip(ps, vs, ms):
            self.AddBody(p, v, m)

    def Update(self):
        for i in range(len(self.ps)):
            p1 = self.ps[i]
            m1 = self.ms[i]

            for j in range(len(self.ps)):
                if i != j:
                    p2 = self.ps[j]
                    m2 = self.ms[j]

                    r = p2 - p1
                    r_norm = np.linalg.norm(r)
                    
                    if r_norm > 0:
                        F = self.G * m1 * m2 / r_norm**2
                        F_vec = F * r / r_norm
                        self.vs[i] += F_vec / m1
    def Draw(self):
        pass