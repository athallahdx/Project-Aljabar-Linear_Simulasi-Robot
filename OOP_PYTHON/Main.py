from robot import Robot
from wheel import Wheel
from kinematic import Kinematic
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_title('3 Omniwheel Robot Simulation', fontweight='bold')

ambatron = Robot(0, 0, 10, edgecolor='red', facecolor='red')
ambatron.add_to_axes(ax)

