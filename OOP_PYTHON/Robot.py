from Wheel import Wheel
from matplotlib.patches import Circle

class Robot(Circle):
    def __init__(self, x=0, y=0, radius=5, edgecolor='red', facecolor='red', **kwargs):
        self.radius = radius
        self.edgecolor = edgecolor
        self.facecolor = facecolor
        self.x = x
        self.y = y
        self.wheel_1 = Wheel(alpha=90, wheel_number=1)
        self.wheel_2 = Wheel(alpha=210, wheel_number=2)
        self.wheel_3 = Wheel(alpha=330, wheel_number=3)
        super().__init__((x, y), radius, edgecolor, facecolor, **kwargs)

    def add_to_axes(self, ax):
        ax.add_patch(self)
        ax.add_patch(self.wheel_1)
        ax.add_patch(self.wheel_2)
        ax.add_patch(self.wheel_3)

    

    # def move_robot(self, robot_linear_velocity, robot_angular_velocity):
    