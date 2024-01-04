__doc__ = "Main method"

#import system libs
import argparse
import sys
from scipy import constants
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl 

#own modules
from examples.plot_example import exec_sample_plot_

print("Hello world\n")

#setup arg parser
arg_parser_ = argparse.ArgumentParser(description="Process some integers.")
arg_parser_.add_argument("pdf_file_out", type=str, help="filename to plot")
arg_parser_.add_argument("sec", type=str, help="sec_argument")
cmd_call_args_ = arg_parser_.parse_args()
#print (cmd_call_args_.pdf_file_out)

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

