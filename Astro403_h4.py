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
fig, ax = plt.subplots(figsize=(7, 5))

## Reads the csv file and drops all the empty values ##
df = pd.read_csv("./rho-P_solar_model.csv", header=[0,1])

df.groupby(level = 0, axis = 1)
ax.plot(df['photosphere']['logRho'],df['photosphere']['logP'])
ax.plot(df['Envelope']['logRho'],df['Envelope']['logP'])
ax.plot(df['Core']['logRho'],df['Core']['logP'])


#for name, df_group in df.groupby(level = 0, axis=1):
#    df_group = df_group[name].dropna()
#    print(df_group)
#    ax.plot(df_group[name][0],df_group[name][1], label=name)
    # Get the dPdrho and plot the fit. Could use scipy.stats linregress
    #avg_run = df_group["logRho"].diff().mean()
    #avg_rise = df_group["logP"].diff().mean()
    #dPdrho = avg_rise/avg_run
    #ax.plot(df_group["logRho"], df_group["logRho"]*dPdrho,
    #        label=f"{name} $\\frac{{dP}}{{d\\rho}}$ = {dPdrho:.3f}")

    
ax.set_xlabel("log")
ax.set_ylabel("log")
ax.set_title("Log of pressure versus log of density of 1  star")
#ax.legend()
fig.tight_layout()
fig.show()
#plt.close("all")


array = df


## Constant ##
fuck = 5.7e9


## I hate tuples and lists and shit is dumb ##
dumb = array.columns
axis_list = list(zip(*dumb))[1]


##Plot 1 ##
rho1 = array.iloc[:,0]
Penis = fuck * (10 ** rho1)**(4/3)

## Slope thingy

def rem(arg):
    if pd.isna(arg) == True:
        return 0
    else:
        return arg

nlist1 = []

for i in array.iloc[:,0]:
    nlist1.append(rem(i))


nlist2= []
for i in array.iloc[:,1]:
    nlist2.append(rem(i))

nlist3= []
for i in array.iloc[:,2]:
    nlist3.append(rem(i))

nlist4= []
for i in array.iloc[:,3]:
    nlist4.append(rem(i))

nlist5= []
for i in array.iloc[:,4]:
    nlist5.append(rem(i))

nlist6= []
for i in array.iloc[:,5]:
    nlist6.append(rem(i))
      

p1 = np.polyfit(nlist1, nlist2, deg =1)  
print("The fitted slope of the line is: ",p1)

#Plotting
plt.figure("Photosphere")
plt.plot(array.iloc[:,0],np.log10(Penis), label = "formula")
plt.plot(array.iloc[:, 0], array.iloc[:, 1], label = "raw data")
plt.xlabel(axis_list[0])
plt.ylabel(axis_list[1]) 
plt.legend()
plt.title("Photosphere")
plt.show()

## Plot 2 ##

rho2 = array.iloc[:,2]
Penis2 = fuck * (10 ** rho2)**(4/3)

p2 = np.polyfit(nlist3,nlist4, deg =1)  
print("The fitted slope of the line is: ",p2)

#Plotting
plt.figure("Envelope")
plt.plot(array.iloc[:, 2], array.iloc[:, 3])
plt.plot(array.iloc[:, 2], np.log10(Penis2))
plt.xlabel(axis_list[2])
plt.ylabel(axis_list[3])
plt.title("Envelope")


## Plot 3 ##

rho3 = array.iloc[:,4]
Penis3 = fuck * (10 ** rho3)**(4/3)

p3 = np.polyfit(nlist5,nlist6 ,deg =1)  
print("The fitted slope of the line is: ",p3)

#Plotting
plt.figure("Core")
plt.plot(array.iloc[:, 4], array.iloc[:, 5])
plt.plot(array.iloc[:, 4], np.log10(Penis3))
plt.xlabel(axis_list[4])
plt.ylabel(axis_list[5])
plt.title("Core")
#plt.show()