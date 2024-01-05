#import system libs
#----
#copy code
#source: https://matplotlib.org/stable/users/explain/quick_start.html
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
#end copy
#----
from scipy import constants

#import own methods
from formulas import calc
from get_arguments import call_arg

#===============
#calling the plot function
def exec_plot():
    #passing all methods with required variables 
    deceleration, in_speed, stopping_time, time, angle, current_velocity, current_distance, total_distance = calc()
    mass, velocity, friction, incline, low_angle, high_angle, filename = call_arg()

    #specifiying the fist plot parameters (position, x, y)
    plt.plot()
    plt.suptitle (f'Results for v={round(in_speed,2)} m/s, m={round(mass,2)} kg, incline={round(incline,2)} deg, my={round(friction,2)}')
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

    #display the plot
    plt.show()

    #export the plot to the main directory 
    plt.savefig(filename)
