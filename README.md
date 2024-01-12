Name: Moritz Golombek
Student ID: S2310787008

------------------------------------------------------------------------------------------------------------

Call Arguments and standard values:
1. -m / --mass:         1000 [kg]
2. -v / --velocity:       50 [km/h]
3. -f / --friction:     0.65 [-]     -> initially included choices 0,1 - 0,65 of commonly used friction coefficients, removed for more flexibility (high downforce, etc.)
4. -a / --inclination:     0 [deg]
5. -d / --descend_limit: -20 [deg]
6. -u / --ascend_limit:   45 [deg]
7. -n / --filename:   example_plot 

------------------------------------------------------------------------------------------------------------

Sample call statements: 
1. Python S2310787008.py --help -> shows all available input options and their short forms.
2. Python S2310787008.py --mass=1000 -> sets vehicle mass to 1000 kg, uses standard values for the rest.
3. Python S2310787008.py --velocity=100 -> sets vehicle speed to 100 km/h, uses standard values for the rest.
...
4. Python S2310787008.py --mass=1000, --velocity=50, --friction=0.65, --inclination=10
5. Python S2310787008.py -m1000 -v50 -f0.65 -a10 -> does exaclty the same as the line above, just in short form
6. Python S2310787008.py --descend_limit=-45, --ascend_limit=45 -> will give the required stopping distance from 100% descend to 100% ascend, standard values for the rest.
7. Python s2310787008.py --mass=1500, --velocity=100 -d=-20 -a=20 -> vehicle mass is 1500 kg, velocity is 100 km/h, range of slopes investigated: -20 to 20 deg

------------------------------------------------------------------------------------------------------------

How the problem is solved: 

1.  The call arguments are processed. This is necessary, as the units used for user convenience during the entering process are not all in suitable Si units.
    Namely the conversion of km/h to m/s is conducted here and a conversion of the incline in degree to radians is conducted. 

2.  The stopping distance is calculated by setting the kinetic energy of the vehicle in motion equal to the Work conducted by the friction over a distance.
    The formulas are Wkin = 1/2*m*v0^2, Wr = my*m*g*d with m = mass, my = friction coefficient, g = gravitational force, d = distance, v0 = initial speed.
    To incorporate also inclines or declines, which affect the stopping distance, the formula for Wr was extended to Wr = s*m*g*(my*cos(a)+sin(a)) with p = angle of incline.
    The final simplification of the formula is: s = v0^2/2*g*(my*cos(p)+sin(p)).

3.  With the stopping distance known, the acceleration (in this case deceleration because of the negative sign) can be calculated. 
    Derived from the 2nd law of motion s = 1/2*a*t^2 and a = vf-v0/2 with a = acceleration the formula a = (vf^2-v0^2)/2*s is derived with vf = final velocity, in this case 0 m/s.

4.  The relation is then used to calculate the stopping time with t = 2*s/v0. 
    The value calculated for the stopping time is then used as boundary range for the plot functions in the linspace-definition.

5.  To show that the mass of a vehicle has a substantial impact in real life braking manouevres the required braking force is also displayed to the user. 
    The formula Fb = m*a with Fb = braking force is used. 

6.  For velocity / time plot, needing a time-dependant velocity function, the relation a = v/t can be used together with the initial velocity v0. 
    The following formula results: v = a*t+v0.

7.  The distance / time plot again uses the 2nd law of motion with the resulting formula being used: s = 1/2*a*t^2+v0*t.

8.  The last step is setting the correct labels and plot settings so the result is displayed correctly. The matplotlib.org help-site was used to find the correct arguments.

9.  Besides the graphs the user can also get the most useful information from the console. The entered variables, stopping distance, deceleration and stopping time are displayed.
    The standard "Rule-of-Thumb" formula for the calculation of an emergency braking distance is also implemented and given as an output for comparison to the user.
    This is done without and with a reaction time, while the calculations above show the distance needed from fully applied brakes to stand-still. 

10.  A stopping distance over time graph was added. This was done by using the formula presented above for the stopping distance with a variable angle. 
    The user can also alter the range of angles calculated by calling the --descend_limit= and --ascend_limit= arguments, shorts: -d & -a. 
    The result is plotted together with the two other graphs.

11. There is no LUT used for the road types and road conditions as there are no hardcoded values allowed. 
    The application could be extended towards this easily though referencing the string-inputs of the user to a if-function through the arg-parser.
    The formula does not account for drag-force and should be seen as a simplification. 
------------------------------------------------------------------------------------------------------------
