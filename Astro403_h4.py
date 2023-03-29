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

df = pd.read_csv('datahw4.csv', header=[0,1])
array = df

#print(array)
## Constant ##
fuck = 5.7e9


## I hate tuples and lists and shit is dumb ##
dumb = array.columns
axis_list = list(zip(*dumb))[1]


##Plot 1 ##
rho1 = array.iloc[:,0]
Penis = fuck * (10 ** rho1)**(4/3)

## Slope thingy
def error(arg):
    if type(arg) == float and pd.isna(arg) == False:
        return arg

nlist1 = []

for i in array.iloc[:,0]:
    nlist1.append(error(i))

nlist1.remove("None")
print(nlist1)
nlist2= []
for i in array.iloc[:,1]:
    nlist2.append(error(i))

print(nlist1)


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

#p2 = np.polyfit(x= array.iloc[:,2], y = array.iloc[:, 3], deg =1)  
#print("The fitted slope of the line is: ",p2)

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

#p3 = np.polyfit(x= array.iloc[:,4], y = array.iloc[:, 5], deg =1)  
#print("The fitted slope of the line is: ",p3)

#Plotting
plt.figure("Core")
plt.plot(array.iloc[:, 4], array.iloc[:, 5])
plt.plot(array.iloc[:, 4], np.log10(Penis3))
plt.xlabel(axis_list[4])
plt.ylabel(axis_list[5])
plt.title("Core")
plt.show()