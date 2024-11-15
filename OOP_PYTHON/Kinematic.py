import numpy as np

class Kinematic:
    def __init__(self, wheel_1, wheel_2, wheel_3):
        self.wheels = [wheel_1, wheel_2, wheel_3]

    def inverse_kinematics(self, vx, vy, wr):
        """
        Calculate the velocity for each wheel based on robot's linear and angular velocity.
        Args:
            vx: Linear velocity in x-direction (m/s)
            vy: Linear velocity in y-direction (m/s)
            wr: Angular velocity of robot (rad/s)
        """
        for wheel in self.wheels:
            # Compute the linear velocity of the wheel
            wheel.linear_velocity = (
                vx * np.cos(wheel.rad) + vy * np.sin(wheel.rad) + wr * wheel.distance
            )
            print(f"Wheel {wheel.wheel_number} Velocity: {wheel.linear_velocity:.2f}")

    # def forward_kinematics(self):
        
