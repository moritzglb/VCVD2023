#import system libs
import argparse
import numpy as np

#===============
#creating method to get user inputs with the help of argparser
def call_arg():
    #setup argparser
    #based on
    #source: https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(description="Process some integers.")
    #listing all call arguments of the program, consisting of mass, velocity, friction, incline, lowest and highest angle and plot filename 
    parser.add_argument("-m", "--mass", type=int, default=1000, help="mass of vehicle in kg")
    parser.add_argument("-v", "--velocity", type=int, default=50, help="initial velocity of vehicle in km/h")
    parser.add_argument("-f", "--friction", type=int, default=0.65, help="friction coefficient of surface")
    parser.add_argument("-a", "--inclination", type=int, default=0, help="slope of surface in deg")
    parser.add_argument("-d", "--descend_limit", type=int, default=-20, help="sets the steepes descend angle to be calculated")
    parser.add_argument("-u", "--ascend_limit", type=int, default=45, help="sets the steepes ascend angle to be calculated")
    parser.add_argument("-n","--filename", type=str, default="example_plot", help="sets the file name for the plot .pdf export")
    args = parser.parse_args()

    #self-control//print out the chosen file name for the graph export 
    #print (args.filename)

    #display input values to user for confirmation
    print ("Values for Calculation:")
    print (f"Vehicle mass is {round(args.mass,2)} kg")
    print (f"Vehicle speed is {round(args.velocity,2)} km/h")
    print (f"Friction coefficient is {round(args.friction,2)}")
    print (f"Slope is {round(args.inclination,2)} deg")
    print (f"Range of angles for the slope is {round(args.descend_limit,2)} to {round(args.ascend_limit,2)} deg")
    print ("")

    #converting all call arguments to variables (ease of use for later methods)
    mass = args.mass
    velocity = args.velocity
    friction = args.friction
    incline = np.radians(args.inclination)
    low_angle = np.radians(args.descend_limit)
    high_angle = np.radians(args.ascend_limit)
    filename = args.filename+".pdf"

    #return all variables needed in other methods
    return mass, velocity, friction, incline, low_angle, high_angle, filename