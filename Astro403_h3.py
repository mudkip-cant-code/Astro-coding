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
plt.ylabel("q (ergs/s/g)")


##   2b   ##
### Each shell has a constant density and that each shell is a thickness of .01

##  Constants
# Volume of shell at each position 
rcm = r * 695700 * 100000
volume = []
for i in range(60):
    if i ==0:
        volume.append(4/3 * np.pi * rcm[0]**3)
    else:
        volume.append(4/3 * np.pi * (rcm[i]**3-rcm[i-1]**3))

Q = q * volume * rho

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


##      Question 3      ##

#Initialize
dxi = .001
steps = 10000
gamma = [1.5,1/.303]
flag = True

#Loops for both values of n
#The inner loop iterates over values of theta and xi
plt.figure("Q3")

for i in gamma:
    xi = 0.001
    theta = 1
    diff = 0                            #The differential in paranthesis
    theta_list = []
    xi_list = []
    flag = True
    j = 0
    
    while flag == True:
                  
        diff += -xi**2 * theta**i * dxi 
        theta += diff/xi**2 * dxi
        xi += dxi
        theta_list.append(theta)
        xi_list.append(xi)
        
        if np.real(theta_list[j]) < 0  and flag == True:
            plt.plot(xi,theta ,"ro")
            print(j)
            print(theta_list[j])
            flag = False
            print(diff/xi**2)
            ## Central pressure and density calculations 
            M_n = -diff
            D_n = (- 3* diff / xi ** 3) ** (-1)
            B_n = D_n ** (1/i-1/3) / (i+1) * (1/M_n) **((i-1)/i) * (1/xi) ** ((3-i) / i)
            rho_c = D_n * 1.989e30 / (4/3 * np.pi * 6.9634e8 ** 3)  
            P_c = (4 * np.pi) ** (1/3) * 6.67e-11 * B_n * 1.989e30 ** (2/3) * rho_c ** (4/3)  
            print("M_n = ", M_n ,"D_n = ", D_n ,"B_n :", B_n)
            print("Central density = ", str(rho_c) + "kg/m^3, Central pressure = ", str(P_c) + "Pa, for gamma = ", str(np.round(i,4)))
        j += 1

    print(xi_list[-1],theta_list[-1])
    plotlabel = "gamma = " + str(np.round(i,4))        
    plt.plot(xi_list, theta_list, label = plotlabel)
    
plt.legend()
plt.xlabel("xi")
plt.ylabel("theta")
plt.grid()
plt.show()