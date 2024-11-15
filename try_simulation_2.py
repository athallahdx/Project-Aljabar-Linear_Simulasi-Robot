import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import pygame
import time
import numpy as np

# Initialize Pygame
pygame.init()

# Initialize the joystick
pygame.joystick.init()

# Check for available joysticks
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)  # First joystick
    joystick.init()
else:
    print("No joystick found!")

# Robot Parameters
RADIUS = 3  # radius of each wheel (rectangle width)
L = 10       # distance from center to each wheel (circle radius)
WIDTH = 5    # width of each wheel (rectangle width)
HEIGHT = 3   # height of each wheel (rectangle height)
a1 = 90     # angle of wheel 1
a2 = 210    # angle of wheel 2
a3 = 330    # angle of wheel 3

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_title('3 Omniwheel Robot Simulation', fontweight='bold')

# Draw a circle to represent the robot body
circle = patches.Circle((0, 0), L, edgecolor='red', facecolor='red')
ax.add_patch(circle)

# Define the robot's speed components
def get_speed_components(v, theta):
    vx = v * np.cos(theta)
    vy = v * np.sin(theta)
    return vx, vy

# Define the wheel velocity function
def wheel_velocity(vx, vy, r, alpha, omega, l):
    velocity = (vx * np.cos(alpha) + vy * np.sin(alpha) + omega * l)
    return velocity

# Function to place rectangles (wheels) around the circle
def add_wheel(angle_degree, distance, wheel_number):
    angle_rad = np.radians(angle_degree)
    xc = distance * np.cos(angle_rad)
    yc = distance * np.sin(angle_rad)
    x = xc-WIDTH/2 
    y = yc-HEIGHT/2

    wheel = patches.Rectangle(
        (x, y),  
        width=WIDTH,  
        height=HEIGHT,  
        angle=angle_degree + 90,  
        color='blue',
        rotation_point=(xc, yc)
    )
    ax.text(xc, yc, f'{wheel_number}', ha='center', va='center', color='white', fontweight='bold')
    
    return wheel

# Add wheels at specified angles
wheels = []
for i, angle in enumerate([a1, a2, a3]):
    wheels.append(add_wheel(angle, L, i + 1))

for wheel in wheels:
    ax.add_patch(wheel)

def create_arrow(x, y, angle, color='black'):
    arrow = patches.Arrow(x, y, L*np.cos(angle), L*np.sin(angle), width=3, color=color)
    return arrow

# Global variable to keep track of the arrow
arrow_patch = None

# Update function for animation
def update(frame):
    global arrow_patch 
    pygame.event.pump()

    x_axis = joystick.get_axis(0)  # X axis
    y_axis = -(joystick.get_axis(1))  # Y axis
    angle_radians = np.arctan2(y_axis, x_axis)
    angle_degrees = np.degrees(angle_radians)

    if arrow_patch is not None:
        arrow_patch.remove()
        arrow_patch = None

    # Set robot's linear speed (v) and angle (theta) for this frame
    v = 3  # Robot speed (m/s)
    theta = np.radians(frame)  # Robot direction (angle in radians)
    omega = 0  # Angular velocity (rad/s)
    
    # Get the speed components for vx and vy
    vx, vy = get_speed_components(v, angle_radians)
    
    # Calculate the wheel velocities for each wheel
    v1 = wheel_velocity(vx, vy, RADIUS, np.radians(0), omega, L)
    v2 = wheel_velocity(vx, vy, RADIUS, np.radians(120), omega, L)
    v3 = wheel_velocity(vx, vy, RADIUS, np.radians(240), omega, L)
    
    # Print the wheel velocities
    print(f"Angle {angle_degrees:.2f}: v1: {v1:.2f}, v2: {v2:.2f}, v3: {v3:.2f}")

    # Update wheel velocities on the plot (display on the wheel)
    for i, wheel in enumerate(wheels):
        wheel.set_facecolor('blue')

    # Update the robot's position based on the speed components
    rads = np.radians(frame)
    arrow_patch = create_arrow(0, 0, angle_radians) 
    ax.add_patch(arrow_patch)

    

# Animate the plot using FuncAnimation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 1), interval=25)

# Display the plot
ax.set_aspect('equal', 'box')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
plt.show()
