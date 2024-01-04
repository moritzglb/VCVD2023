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
#listing all cll arguments of the program, consisting of mass, velocity, friction and inclination 
parser.add_argument("--mass", type=int, default=1000, help="mass of vehicle")
parser.add_argument("--velocity", type=int, default=50, help="initial velocity of vehicle")
parser.add_argument("--friction", type=int, default=0.65, choices=(0.1, 0.2, 0.4, 0.65), help="friction coefficient of surface")
parser.add_argument("--inclination", type=int, default=0, choices=range(0,100), help="inclination of surface")
args = parser.parse_args()

print ("Your chosen vehicle mass is",args.mass)
print ("Your chosen vehicle speed is",args.velocity)
print ("Your chosen friction coefficient is",args.friction)
print ("Your chosen inclination is",args.inclination)

#===============
#brake distance calculation method
def distance_method():
  distance_method.__doc__ = "calculation of braking distance"
  
#velocity over time under breaking
def velocity_method():
  velocity_method.__doc__ = "calculation of braking velocity"

#===============
# do work and call a methode
#method()

#terminate program
sys.exit()

