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

# Example of reading joystick axis and button states
while True:
    pygame.event.pump()  # Process events to update joystick status
    
    # Get axis values (e.g., left joystick)
    x_axis = joystick.get_axis(0)  # X axis
    y_axis = -(joystick.get_axis(1))  # Y axis
    angle_radians = np.arctan2(y_axis, x_axis)
    angle_degrees = np.degrees(angle_radians)
    print(f"Axis X: {x_axis}, Axis Y: {y_axis}")
    print(f"Angle (radians): {angle_radians}, Angle (degrees): {angle_degrees}")
    
    
    pygame.time.wait(500)  # Delay for 100 ms


