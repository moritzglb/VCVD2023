#import system libs
#based on
#source: https://matplotlib.org/stable/users/explain/quick_start.html
import matplotlib.pyplot as plt
import numpy as np

#import own methods
from formulas import calc
from get_arguments import call_arg

#===============
#calling the plot function
def exec_plot():
    """convert all calculated values into plots"""
    #passing all methods with required variables
    in_speed, time, angle, current_velocity, current_distance, total_distance = calc()
    mass, velocity, friction, incline, low_angle, high_angle, filename = call_arg()

    #setting the plot title, including the key values used
    plt.figure(figsize=(10,8))
    plt.suptitle (f'Results for v={round(in_speed,2)} m/s, m={round(mass,2)} kg, incline={round(np.degrees(incline))} deg, my={round(friction,2)}')

    #specifiying the fist plot parameters (position, x, y)
    plt.subplot(2,2,1)
    plt.plot (time, current_velocity)
    #labeling the first plot (title, axis, adding grid)
    plt.title ('Velocity over Time')
    plt.xlabel ('time [s]')
    plt.ylabel ('velocity [m/s]')
    plt.grid (True)

    #specifiying the second plot parameters (position, x, y)
    plt.subplot(2,2,2)
    plt.plot (time, current_distance)
    #labeling the second plot (title, axis, adding grid)
    plt.title ('Distance over Time')
    plt.xlabel ('time [s]')
    plt.ylabel ('distance [m]')
    plt.grid (True)

    #specifiying the second plot parameters (position, x, y)
    plt.subplot(2,1,2)
    plt.plot (np.degrees(angle),total_distance)
    #labeling the second plot (title, axis, adding grid)
    plt.title ('Stopping distance over Incline')
    plt.xlabel ('angle [deg]')
    plt.ylabel ('stopping distance [m]')
    plt.grid (True)

    #make sure no overlaps of axes happen
    plt.tight_layout()

    #export the plot to the main directory
    plt.savefig(filename, dpi=300, format='pdf')

    #display the plot if user likes to
    plt.show()

