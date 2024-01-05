#import system libs
import numpy as np
from scipy import constants

#import own methods
from get_arguments import call_arg

#===============
#create method to do calculations, this is where the main formulas are 
def calc():
    #passing all methods with required variables
    mass, velocity, friction, incline, low_angle, high_angle, filename = call_arg()

    #converts input to correct units for speed calculation (km/h -> m/s)
    in_speed = velocity*constants.kmh #[m/s]

    #self-control//confirm intermediate values (previously problem with rad vs. deg)      
    #print (velocity, incline, friction, low_angle, high_angle, np.cos(low_angle), np.cos(high_angle), np.cos(incline))

    #calculate stopping distance for braking manoeuvre in m
    stopping_distance = (in_speed**2)/(2*constants.g*(friction*np.cos(incline)+np.sin(incline)))
    print ("The stopping distance is", stopping_distance,"m")

    #implementation of "Rule-of-Thumb" (emergency braking). Printing the braking distance and overall distance with reaction time of 3 s
    reaction_time = 3 #[s]
    distance_rot = 0.5*(velocity/10)**2
    print ("The emergency brake stopping distance according to the RoT would be", distance_rot, "m (including reaction time:", distance_rot+(velocity/10)*reaction_time, "m)")
    print ("")

    #calculate deceleration during braking manoeuvre in m/s^2
    deceleration = (0**2-in_speed**2)/(2*stopping_distance)
    print ("The deceleration is", deceleration/constants.g, "G, or", deceleration, "m/s^2")

    #calculate time needed for braking manoeuvre in s 
    stopping_time = 2*stopping_distance/in_speed
    print ("The time needed to stop is", stopping_time, "s")
    print ("")

    #setting the boundaries for the x-axis to the duration of the braking manoeuvre in s (start of braking to standstill)
    time = np.linspace(0,stopping_time)
    #setting the boundaries for the x-axis of the distance / gradient plot in deg (steepest decline to steepest incline)
    angle = np.linspace(low_angle,high_angle)

    #velocity during breaking manoeuvre
    current_velocity = deceleration*time+in_speed

    #distance travelled during breaking manoeuvre in m 
    current_distance = (deceleration*time**2)/2+in_speed*time

    #required stopping distance depending on angle of slope in m 
    total_distance = (in_speed**2)/(2*constants.g*(friction*np.cos(angle)+np.sin(angle)))

    #return all variables needed in other methods
    return deceleration, in_speed, stopping_time, time, angle, current_velocity, current_distance, total_distance