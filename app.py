help = """
Help:
- H: Shows this list of interactions
- Q: Quit application
- Space: Pause/Resume simulation
- R: Reset simulation
- WASD: Pan camera
- I: Zoom in
- O: Zoom out
- N: Add new body + WASD for positioning + N again for confirmation
- T: Toggle trails
"""

from shell import Shell
from gravity import GravitySim
from camera import Camera

class App:
    def __init__(self):
        self.sim = GravitySim()
        self.shell = Shell()
        self.cam = Camera()

        self.running = True
        self.active  = True  # Paused/unpaused
        self.adding  = False # Whether a new body is being added
        self.trails  = True  # Whether trails are displayed

    def Run(self):
        self.shell.cmdloop()

        while self.running:
            self._Events()
            self._Update()
            self._Draw()
    
    def _Events(self):
        while self.smth.PollEvents(): # Poll events from SSH server
            match event:
                case "N":
                    self.adding = True
                case _:
                    pass

    def _Update(self):
        self.sim.Update()
    def _Draw(self):
        pass