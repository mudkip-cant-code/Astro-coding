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
