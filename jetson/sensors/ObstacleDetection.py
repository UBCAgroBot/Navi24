import matplotlib as plt
import numpy as np
import math

class SemiCircleCheck:
       
    def __init__(self, robot_radius= 0.5, d_T = 0.55):
        self.robot_radius = robot_radius
        self.d_T = d_T
        self.fig, self.ax = plt.subplots()
        
    #private functions
    #requires: r, theta values from the lidar and given maximum measured width of the robot in metres
    #draws a semi-circle on the lidar ray that is a possible path
    def drawSemiCircle(self, r, theta, robot_radius, ax):
        centre_x = r * np.cos(theta)
        centre_y = r * np.sin(theta)

        semi_circle_theta = np.linspace(0, np.pi, 100)

        x = centre_x + robot_radius * np.cos(semi_circle_theta)
        y = centre_y + robot_radius * np.sin(semi_circle_theta)


        ax.plot(x, y, color='blue')

        ax.set_aspect('equal')
        ax.set_xlim(-robot_radius - 1, robot_radius + 1)
        ax.set_ylim(-1, robot_radius + 1)

    #Function to find gaps(discontinuities) in lidar data
    def find_gaps(self, lidar_data):
        gaps = []
        
        for i in range(len(lidar_data) - 1):
            r1, theta1 = lidar_data[i]
            r2, theta2 = lidar_data[i+1]

            distance = abs(r2 - r1)

            if distance > self.d_T:
                gaps.append((r1, theta1, r2, theta2))
        return gaps
    
    def passable_semicircles(self, left_r, left_theta, right_r, right_theta):

        
        
        
    
    #requires: lidar_data that has radius and theta as polar coordinates
    #uses a drawSemiCircle for the data that is a an obstacle
    def draw_lidar_data(self, lidar_data, ax):
        
        gaps = self.find_gaps(lidar_data)

        for r1, theta1, r2, theta2 in gaps:

            if self.passable_semicircles(r1, theta1, r2, theta2):
                self.drawSemiCircle(r1, theta1, self.robot_radius, self.ax)
                self.drawSemiCircle(r2, theta2, self.robot_radius, self.ax)

            else:
                self.drawSemiCircle(r1, theta1, self.robot_radius, self.ax)
                self.drawSemiCircle(r2, theta2, self.robot_radius, self.ax)
            
        plt.show()
        

        

    


    