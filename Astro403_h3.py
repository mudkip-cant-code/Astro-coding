##Astro 403 Ass 3
##I dont like to comment am lazy
#Imports 
import matplotlib.pyplot as plt 
import numpy as np

#   White backgrounds are for losers    #
plt.style.use('dark_background')
###     Question 2    ####

#   Variable
r = np.arange(0,0.6, 0.01)


#   Constants
R = 1                   #solar radius              
rho_c = 176
T_c = 17
X = .707


#   Equations 
rho = rho_c * 10**(-4*r/R)
T = T_c*10**(-1.2*r/R)
q = 2.54e6 * X**2 * rho * T**(-2/3) * np.exp(-33.81/T**(1/3))

drop = False
q_0 = q[0]*10**-3

plt.figure("2(a)")

for i in  range(r.size):
    if q[i] < q_0 and drop == False:
        print("Dropped three orders of magnitudes at: ", r[i],q[i])
        plt.plot(r[i],q[i],'ro', label = "Dropped 3 Orders of Magnitude")
        drop = True

## !PLOTING IS FUN! ## (SNORTS 3 lbs of coke) why is this not working
plt.plot(r,q,'g-')
plt.grid()
plt.legend()
plt.xlabel("Solar Radius")
plt.ylabel("q whatever that is")


##   2b   ##
### Each shell has a constant density and that each shell is a thickness of .01

##  Constants or whatever
# Volume of shell at each position 
rcm = r * 695700 * 100000
volume = []
for i in range(60):
    if i ==0:
        volume.append(4/3 * np.pi * rcm[0]**3)
    else:
        volume.append(4/3 * np.pi * (rcm[i]**3-rcm[i-1]**3))

Q = q*volume*rho

plt.figure("2(b)")
plt.plot(r, Q, "g")
plt.xlabel("Radius of Shell (cm)")
plt.ylabel("Total Energy in Shell (ergs/s)")
plt.grid()


l_real = 3.85e33
luminosity = 0

## This sums the energy each shell creates to get total luminosity
for i in range(r.size):
    luminosity += Q[i]

print("The total luminosity we calculate is: ",luminosity, "This is ",l_real - luminosity, "less then the real value." )

## Showing the inner 25% is 99% of the total energy

## 99% of the total luminosity 
lum99 = luminosity * .99
lum = 0
flag = False
point = 0

##  Will do basically the same thing here but once we reach 99% 
##  of total luminosity I print the percent of the total volume at that point.
for i in range(r.size):
    if lum >= lum99 and flag == False:
        print("99% of the total luminosity is created within the inner ",volume[i]/volume[-1]*100, "of the volume")
        point = i
        flag = True
        
        
    lum += Q[i]

plt.figure("2(b)")
plt.plot(r[point], Q[point],"ro", label= "99% of the total luminosity")
plt.legend()
#plt.show()


##      Question 3      ##

### JUST SOLVE THE LANE EMDEN EQUATION ###

gama_a = 5/3
gama_s = 1.303

#Step (bro what are you doing)
dxi = .0001
steps = 10000
n = [1.5,1/.303]

for i in range(2):
    xi = 0
    theta = 1
    diff = 0                            #The differential in paranthesis
    theta_list = np.empty(steps)
    xi_list = np.empty(steps)

    for i in range(steps):
        diff += xi**2 * theta
        
