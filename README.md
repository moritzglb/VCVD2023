Name: Moritz Golombek
Student ID: S2310787008

Sample call statement: 
Python S2310787008.py --mass=1000, --velocity=50, --friction=0.65, --inclination=10

Standard values:
- mass:         1000 [kg]
- velocity:     50 [km/h]
- friction:     0.65 [-]
- inclination:  0 [deg]

How the problem is solved: 

1.  The call arguments are processed. This is necessary, as the units used for user convenience during the entering process are not all in suitable Si units.
    Namely the conversion of km/h to m/s is conducted here and a conversion of the incline in degree to radians is conducted. 

2.  The stopping distance is calculated by setting the kinetic energy of the vehicle in motion equal to the Work "conducted" by the friction over a distance.
    The formulas are Wkin = 1/2*m*v0^2, Wr = my*m*g*d with m = mass, my = friction coefficient, g = gravitational force, d = distance, v0 = initial speed.
    To incorporate also inclines or declines, which affect the stopping distance, the formula for Wr was extended to Wr = s*m*g*(my*cos(a)+sin(a)) with p = angle of incline.
    The final simplification of the formula is: s = v0^2/2*g*(my*cos(p)+sin(p)).

3.  With the stopping distance known, the acceleration (in this case deceleration because of the negative sign) can be calculated. 
    Derived from the 2nd law of motion s = s0 + v0*t + 1/2*a*t^2 with a = acceleration the formula a = (vf^2-v0^2)/2*s is derived with vf = final velocity, in this case 0 m/s.

4.  In relation is then used to calculated the stopping time with t = 2*s/v0. 
    The value calculated for the stopping time is then used as boundary range for the plot functions in the linspace-definition.

5.  For velocity / time plot, needing a time-dependant velocity function, the relation a = v/t can be used together with the initial velocity v0. 
    The following formula results: v = a*t+v0.

6.  The distance / time plot again uses the 2nd law of motion with the resulting formula being used: s = 1/2*a*t^2+v0*t.

7.  The last step is setting the correct labels and plot settings so the result is displayed correctly. The matplotlib.org help-site was used to find the correct arguments.

8.  Besides the graphs the user can also get the most useful information from the console. The entered variables, stopping distance, deceleration and stopping time are displayed.
    The standard "Rule-of-Thumb" formula for the calculation of an emergency braking distance is also implemented and given as an output for comparison to the user.
    This is done without and with a reaction time, while the calculations above show the distance needed from fully applied brakes to stand-still. 
