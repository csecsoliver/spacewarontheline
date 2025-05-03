
from victor import Victor
import gevent
from gevent import monkey; monkey.patch_all()
import time
game_vars = {
    "sprites": [],
    
}
speed_of_shit = 10


class Sprite:
    def __init__(self, x, y, image, angle = 0, scale=1):
        self.x = x
        self.y = y
        self.angle
        self.scale = scale
        self.movementvector = Victor(0, 0)
        self.visibility = True
        self.image = image ## point cloud or something
    
    def set_position(self, x, y, angle = None):
        self.x = x
        self.y = y
        if angle is not None:
            self.angle = angle
        self.movementvector = Victor(0, 0)
    
    def tick(self, dt = 1):
        self.x += self.movementvector.x * dt
        self.y += self.movementvector.y * dt
        if self.x > 813:
            self.x = -12
        if self.x <= -13:
            self.x = 812
        if self.y > 613:
            self.y = -12
        if self.y <= -13:
            self.y = 612
        
    