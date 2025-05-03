import math
class Victor:
    ## Vector handling class
    ## This class is used to handle 2D vectors
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
    def add(self, other):
        ## Add two vectors together
        ## Returns and modifies the current vector
        self.x += other.x
        self.y += other.y
        return self
    
    def sub(self, other):
        ## Subtract two vectors
        ## Returns and modifies the current vector
        self.x -= other.x
        self.y -= other.y
        return self
    
    def mul(self, factor):
        ## Multiply by a scalar
        ## Returns and modifies the current vector
        self.x *= factor
        self.y *= factor
        return self
    def rotate(self, angle):
        ## Rotate the vector by an angle in degrees
        ## Returns and modifies the current vector
        angle = math.radians(angle)
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x = x
        self.y = y
        return self
    def length(self):
        ## Returns the length of the vector
        return math.sqrt(self.x**2 + self.y**2)
    def normalize(self):
        ## Normalize the vector to length 1
        ## Returns and modifies the current vector
        length = self.length()
        if length == 0:
            return self
        self.x /= length
        self.y /= length
        return self
        
    