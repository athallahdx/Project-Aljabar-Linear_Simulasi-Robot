import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

class Wheel(Rectangle):
    def __init__(self, alpha, wheel_number, distance=10, width=5, height=3, color='blue', **kwargs):
        self.alpha = alpha
        self.width = width
        self.height = height
        self.color = color
        self.rad = np.radians(self.alpha)
        self.wheel_number = wheel_number
        self.xc = distance * np.cos(self.rad)
        self.yc = distance * np.sin(self.rad)
        self.x = self.xc - self.width/2
        self.y= self.yc - self.height/2
        self.rotation_point = (self.xc, self.yc)
        self.angle = alpha+90
        super().__init__((self.x, self.y), self.width, self.height, angle=self.angle, color=self.color, **kwargs)
        self.linear_velocity = 0
        self.angular_velocity = 0

