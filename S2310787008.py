__doc__ = "Main method for the calculations"

#import system libs
import argparse
import sys
import math
#----
#copy code
#source: https://matplotlib.org/stable/users/explain/quick_start.html
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
#end copy
#----
from scipy import constants

#own modules
#from examples.plot_example import exec_sample_plot_

#setup argparser
#based on
#source: https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description="Process some integers.")
#listing all call arguments of the program, consisting of mass, velocity, friction and inclination 
parser.add_argument("--mass", type=int, default=1000, help="mass of vehicle in kg")
parser.add_argument("--velocity", type=int, default=50, help="initial velocity of vehicle in km/h")
parser.add_argument("--friction", type=int, default=0.65, choices=(0.1, 0.2, 0.4, 0.65), help="friction coefficient of surface")
parser.add_argument("--inclination", type=int, default=0, help="inclination of surface in deg")
args = parser.parse_args()

#display input values to user for confirmation
print ("Your chosen vehicle mass is",args.mass, "kg")
print ("Your chosen vehicle speed is",args.velocity, "km/h")
print ("Your chosen friction coefficient is",args.friction)
print ("Your chosen inclination is",args.inclination, "deg")

#convert inputs to correct units
in_speed = args.velocity*constants.kmh
incline = math.radians(args.inclination)

#calculate stopping distance for braking manoeuvre
stopping_distance = (in_speed**2)/(2*constants.g*(args.friction*math.cos(incline)+math.sin(incline)))
print ("The stopping distance is", stopping_distance,"m")

distance_rot = 0.5*(args.velocity/10)**2
print ("The emergency brake stopping distance according to the RoT would be", distance_rot, "m (including reaction time:", distance_rot+(args.velocity/10)*3, "m)")

#calculate deceleration during braking manoeuvre
deceleration = (0**2-in_speed**2)/(2*stopping_distance)
print ("The deceleration is", deceleration/constants.g, "G, or", deceleration, "m/s^2")

#calculate time needed for braking manoeuvre
stopping_time = 2*stopping_distance/in_speed
print ("The time needed to stop is", stopping_time, "s")

#setting the length of the x-axis to the duration of the braking manoeuvre
time = np.linspace(0,stopping_time)

#===============
#velocity during breaking manoeuvre
def current_velocity(time):
  current_velocity.__doc__ = "calculation of the current velocity during braking"
  return deceleration*time+in_speed

#===============
#distance traveled during breaking manoeuvre
def current_distance(time):
  current_distance.__doc__="calculation of the distance traveled so far under braking"
  return (deceleration*time**2)/2+in_speed*time

#def distance_rot(time):
#  distance_rot.__doc__="calculation of the distance required according to Rule of Thumb"
#  return 

#===============
#supplying the desired graph plot settings
#based on
#source: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
fig, (ax1,ax2) = plt.subplots(1,2)
ax1.grid (True)
ax2.grid (True)
ax1.plot(time, current_velocity(time))
ax2.plot(time, current_distance(time), distance_rot)
ax1.set_xlabel ('time [s]')
ax2.set_xlabel ('time [s]')
ax1.set_ylabel ('velocity [m/s]')
ax2.set_ylabel ('distance [m]')
ax1.set_title ('Velocity over Time')
ax2.set_title ('Distance over Time')
plt.show()

#terminate program
sys.exit()

