__doc__ = "Main method"

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
parser.add_argument("--mass", type=int, help="mass of vehicle")
parser.add_argument("--velocity", type=int, help="initial velocity of vehicle")
parser.add_argument("--friction", type=int, help="friction coefficient of surface")
parser.add_argument("--inclination", type=int, help="inclination of surface")
args = parser.parse_args()

print (args.mass)

#===============
# a method
def main_method():
  main_method.__doc__ = "sample main method"
# exec_sample_plot_(cmd_call_args_.pdf_file_out)

#===============
# do work and call a methode
main_method()

#terminate program
sys.exit()

