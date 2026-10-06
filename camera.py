# Interactions:
# - WASD: Pan camera
# - I: Zoom in
# - O: Zoom out

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 1.0
    
    def PanLeft(self):
        self.x -= 10
    def PanRight(self):
        self.x += 10
    def PanUp(self):
        self.y -= 10
    def PanDown(self):
        self.y += 10

    def ZoomIn(self):
        self.zoom *= 1.2
    def ZoomOut(self):
        self.zoom /= 1.2