import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Robot Parameters
RADIUS = 0.3  # radius of each wheel (rectangle width)
L = 0.5       # distance from center to each wheel (circle radius)

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_title('3 Omniwheel Robot Simulation', fontweight='bold')

# Draw a circle to represent the robot body
circle = patches.Circle((0, 0), L, edgecolor='r', facecolor='red')
ax.add_patch(circle)

def get_speed_components(v, theta):
    vx = v * np.cos(theta)
    vy = v * np.sin(theta)
    return vx, vy

def wheel_velocity(vy, vx,  r, alpha, omega, l):
    velocity = (vx*np.cos(alpha) + vy*np.sin(alpha) + omega*l)/r
    return velocity

# def draw_arrow(velocity, wheel):

# Function to place rectangles (wheels) around the circle
def add_wheel(angle_degree, distance):
    # Convert angle to radians
    angle_rad = np.radians(angle_degree)
    
    # Calculate wheel center position based on angle
    x = distance * np.cos(angle_rad)
    y = distance* np.sin(angle_rad)
    
    # Define rectangle representing the wheel
    if(angle_degree == 0):
        wheel = patches.Rectangle(
            (x+0.05, y-0.12),  
            width=0.3,  
            height=0.15,  
            angle=angle_degree + 90,  
            color='blue'
        )
        cx, cy = wheel.get_center()
        ax.text(cx, cy, '1', ha='center', va='center', color='white', fontweight='bold')
    
    elif(angle_degree == 120):
        wheel = patches.Rectangle(
            (x, y+0.05),  
            width=0.3,  
            height=0.15,  
            angle=angle_degree + 100,  
            color='blue'
        )
        cx, cy = wheel.get_center()
        ax.text(cx, cy, '2', ha='center', va='center', color='white', fontweight='bold')

    elif(angle_degree == 240):
        wheel = patches.Rectangle(
            (x-0.04, y-0.04),  
            width=0.3,  
            height=0.15,  
            angle=angle_degree + 100,  
            color='blue'
        )
        cx, cy = wheel.get_center()
        ax.text(cx, cy, '3', ha='center', va='center', color='white', fontweight='bold')
        
    ax.add_patch(wheel)

# Add wheels at specified angles
add_wheel(0, L)
add_wheel(120, L)
add_wheel(240, L)

# Set aspect and limits for the plot
ax.set_aspect('equal', 'box')
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

while True:
    for degree, velocity in zip(range(0, 360), range(0, 10)):
        rad = np.radians(degree)
        vel = velocity/10
        # Calculate the wheel velocities
        vx, vy = get_speed_components(vel, np.radians(degree))
        v1 = wheel_velocity(vy, vx, RADIUS, np.radians(0), 0, L)
        v2 = wheel_velocity(vy, vx, RADIUS, np.radians(120), 0, L)
        v3 = wheel_velocity(vy, vx, RADIUS, np.radians(240), 0, L)
        print("v1: ", v1, "v2: ", v2, "v3: ", v3)  
        # Draw the robot body

# Display the plot
plt.show()