__doc__ = "Main method for the calculations"

#import system libs
import argparse
import sys
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
parser.add_argument("-m", "--mass", type=int, default=1000, help="mass of vehicle in kg")
parser.add_argument("-v", "--velocity", type=int, default=50, help="initial velocity of vehicle in km/h")
parser.add_argument("-f", "--friction", type=int, default=0.65, help="friction coefficient of surface")
parser.add_argument("-a", "--inclination", type=int, default=0, help="inclination of surface in deg")
parser.add_argument("-d", "--low_angle", type=int, default=-20, help="sets the steepes descend angle to be calculated")
parser.add_argument("-u", "--high_angle", type=int, default=45, help="sets the steepes ascend angle to be calculated")
args = parser.parse_args()

#display input values to user for confirmation
print ("Values for Calculation:")
print ("Vehicle mass is",args.mass, "kg")
print ("Vehicle speed is",args.velocity, "km/h")
print ("Friction coefficient is",args.friction)
print ("Slope is",args.inclination, "deg")
print ("Range of angles for the slope is", args.low_angle, "to", args.high_angle, "deg")
print ("")

#convert inputs to correct units
in_speed = args.velocity*constants.kmh
incline = np.radians(args.inclination)

#calculate stopping distance for braking manoeuvre
stopping_distance = (in_speed**2)/(2*constants.g*(args.friction*np.cos(incline)+np.sin(incline)))
print ("The stopping distance is", stopping_distance,"m")

distance_rot = 0.5*(args.velocity/10)**2
print ("The emergency brake stopping distance according to the RoT would be", distance_rot, "m (including reaction time:", distance_rot+(args.velocity/10)*3, "m)")
print ("")

#calculate deceleration during braking manoeuvre
deceleration = (0**2-in_speed**2)/(2*stopping_distance)
print ("The deceleration is", deceleration/constants.g, "G, or", deceleration, "m/s^2")

#calculate time needed for braking manoeuvre
stopping_time = 2*stopping_distance/in_speed
print ("The time needed to stop is", stopping_time, "s")

#setting the length of the x-axis to the duration of the braking manoeuvre
time = np.linspace(0,stopping_time)
angle = np.linspace(args.low_angle,args.high_angle)
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

def total_distance(angle):
  total_distance.__doc__="calculation of the total stopping distance depending on the incline"
  return  (in_speed**2)/(2*constants.g*(args.friction*np.cos(np.radians(angle))+np.sin(np.radians(angle))))

#===============
#supplying the desired graph plot settings
#based on
#source: https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
plt.subplot(2,2,1)
plt.plot (time, current_velocity(time))
plt.title ('Velocity over Time')
plt.xlabel ('time [s]')
plt.ylabel ('velocity [m/s]')
plt.grid (True)
plt.subplot(2,2,2)
plt.plot (time, current_distance(time), distance_rot)
plt.title ('Distance over Time')
plt.xlabel ('time [s]')
plt.ylabel ('distance [m]')
plt.grid (True)
plt.subplot(2,1,2)
plt.plot (angle,total_distance(angle))
plt.title ('Stopping distance over Incline')
plt.xlabel ('angle [deg]')
plt.ylabel ('stopping distance [m]')
plt.grid (True)
#plt.show()

#terminate program
sys.exit()

