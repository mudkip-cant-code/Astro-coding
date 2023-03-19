##Astro 403 Ass 3
##I dont like to comment am lazy
#Imports 
import matplotlib.pyplot as plt 
import numpy as np

#   White backgrounds are for losers    #
plt.style.use('dark_background')

###     Question 3    ####

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
plt.show()
