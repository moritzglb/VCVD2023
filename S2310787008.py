#import system libs
import sys 

#import own methods
from graph_export import exec_plot

#===============
#creating the main method, where all relevant "subfunctions" are called
def main_method(): 
    exec_plot()
    #self-control//action upon completion
    #print ("Done!")

#===============
#executing the main method 
main_method()

sys.exit()