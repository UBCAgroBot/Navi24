import matplotlib.pyplot as plt
import numpy as np

class SemiCircleCheck:
       
    def __init__(self, robot_radius=0.5, d_T=0.55):
        self.robot_radius = robot_radius
        self.d_T = d_T
        self.fig, self.ax = plt.subplots()
        
    def drawSemiCircle(self, center_x, center_y, radius, ax, color='blue'):
        #Draws a semicircle given a center and radius.
        semi_circle_theta = np.linspace(0, np.pi, 100)
        x = center_x + radius * np.cos(semi_circle_theta)
        y = center_y + radius * np.sin(semi_circle_theta)
        ax.plot(x, y, color=color)

    def find_gaps(self, lidar_data):
        #Identifies gaps in the lidar data where the distance exceeds the threshold d_T. 
        gaps = []
        for i in range(len(lidar_data) - 1):
            r1, theta1 = lidar_data[i]
            r2, theta2 = lidar_data[i + 1]
            distance = abs(r2 - r1)
            if distance > self.d_T:
                gaps.append((r1, theta1, r2, theta2))
        return gaps
    
    def is_point_in_semicircle(self, point_x, point_y, center_x, center_y, radius):
        #Checks if a point (point_x, point_y) falls within a semicircle centered at (center_x, center_y). 
        distance = np.sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)
        return distance <= radius

    def check_gap_passability(self, r1, theta1, r2, theta2, lidar_data):
        # Checks if a gap between two points is passable by ensuring no obstacles are within the semicircles. 
        # Calculate semicircle centers for both points in the gap
        left_x, left_y = r1 * np.cos(theta1), r1 * np.sin(theta1)
        right_x, right_y = r2 * np.cos(theta2), r2 * np.sin(theta2)
        
        # Check for obstacles within the semicircles around each point in the gap
        passable = True
        for r, theta in lidar_data:
            obstacle_x = r * np.cos(theta)
            obstacle_y = r * np.sin(theta)
            if self.is_point_in_semicircle(obstacle_x, obstacle_y, left_x, left_y, self.robot_radius) or \
               self.is_point_in_semicircle(obstacle_x, obstacle_y, right_x, right_y, self.robot_radius):
                passable = False
                break
        return passable
        
    def draw_lidar_data(self, lidar_data):
       # Draws lidar data with semicircles around passable gaps. 
        gaps = self.find_gaps(lidar_data)

        for r1, theta1, r2, theta2 in gaps:
            left_x, left_y = r1 * np.cos(theta1), r1 * np.sin(theta1)
            right_x, right_y = r2 * np.cos(theta2), r2 * np.sin(theta2)

            # Check gap passability
            if self.check_gap_passability(r1, theta1, r2, theta2, lidar_data):
                color = 'green'  # Passable
            else:
                color = 'red'  # Not passable

            # Draw semicircles at each gap endpoint
            self.drawSemiCircle(left_x, left_y, self.robot_radius, self.ax, color=color)
            self.drawSemiCircle(right_x, right_y, self.robot_radius, self.ax, color=color)
            
            # Draw a line between gap endpoints to show the gap
            self.ax.plot([left_x, right_x], [left_y, right_y], color=color, linestyle='--')

        plt.show()
        
if __name__ == "__main__":
    # Example lidar data including both passable and impassable gaps
    lidar_data = [
        (1.0, np.pi / 6), (2.0, np.pi / 4), (2.1, np.pi / 3.5),
        (1.5, np.pi / 2), (2.8, np.pi / 1.5), (1.0, np.pi / 1.3),
        (3.0, np.pi / 1.2), (1.0, np.pi / 1.05), (2.2, np.pi)
    ]

    # Create an instance of SemiCircleCheck
    semi_circle_checker = SemiCircleCheck(robot_radius=0.5, d_T=0.5)

    # Visualize the lidar data and check for passable gaps
    semi_circle_checker.draw_lidar_data(lidar_data)
