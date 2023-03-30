#Astro403_h4
##SO help me god

## Imports 
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

## Changing directory ##
os.chdir("/Users/jonthanwarkentin/Desktop")

## Dark background == cool :sunglasses:
plt.style.use('dark_background')


## Reads the csv file and drops all the empty values ##
df = pd.read_csv("./rho-P_solar_model.csv", header=[0,1])
df.groupby(level = 0, axis = 1)

## FUCK FOR LOOPS IMA DO THIS THE LONG WAY BC IM OVER IT



#Photo sphere plot
name = 'photosphere'
print(name)
df_Ph = df[name].dropna()
plt.figure(name)
plt.plot(df_Ph['logRho'],df_Ph['logP'])
plt.xlabel('logRho')
plt.ylabel('logP')
plt.title(name)
print("SLope thingy ma bob:", np.polyfit( df_Ph['logRho'],df_Ph['logP'] ,deg =1))
## Formula
fuck = 5.7e9
Penis = fuck * (10 ** df_Ph['logRho'])**(4/3)
plt.plot(df_Ph['logRho'],np.log10(Penis), label = "formula")
print("SLope thingy ma bob:", np.polyfit( df_Ph['logRho'],np.log10(Penis) ,deg =1))



## Envelope
name = 'Envelope'
print(name)
df_Ph = df[name].dropna()
plt.figure("Envelope")
plt.figure(name)
plt.plot(df_Ph['logRho'],df_Ph['logP'])
plt.xlabel('logRho')
plt.ylabel('logP')
plt.title("Envelope")
Penis = fuck * (10 ** df_Ph['logRho'])**(4/3)
plt.plot(df_Ph['logRho'],np.log10(Penis), label = "formula")

print("SLope thingy ma bob:", np.polyfit( df_Ph['logRho'],df_Ph['logP'] ,deg =1))
print("SLope thingy ma bob:", np.polyfit( df_Ph['logRho'],np.log10(Penis) ,deg =1))

print("Density,end :",10**df_Ph['logRho'][0],"Pressure, end:",10**df_Ph['logP'][0])
print("Density, begining:",10**df_Ph['logRho'][279],"Pressure, core:",10**df_Ph['logP'][279])


##PART B
#Constants 
rho_top = 10**df_Ph['logRho'][0]
P_top = 10**df_Ph['logP'][0]
rho_bot = 10**df_Ph['logRho'][279]
P_bot = 10**df_Ph['logP'][279]

G = 6.67e-11
Rsun = 6.96e8
Msun = 1.989e30
a = .1

print("Our mixing length at the bot is:  ", a*P_bot*(.65*Rsun)**2/(rho_bot*G*Msun*.97))
print("Our mixing length at the top is:  ", a*P_top*(.999*Rsun)**2/(rho_top*G*Msun))


## Core
name = 'Core'
print(name)
df_Ph = df[name].dropna()
plt.figure("Core")
plt.figure(name)
plt.plot(df_Ph['logRho'],df_Ph['logP'])
plt.xlabel('logRho')
plt.ylabel('logP')
plt.title("Core")
Penis = fuck * (10 ** df_Ph['logRho'])**(4/3)
plt.plot(df_Ph['logRho'],np.log10(Penis), label = "formula")
print("SLope thingy ma bob:", np.polyfit( df_Ph['logRho'],df_Ph['logP'] ,deg =1))
print("SLope thingy ma bob:", np.polyfit( df_Ph['logRho'],np.log10(Penis) ,deg =1))

plt.show()
