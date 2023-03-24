import os
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd

os.chdir("/Users/jonthanwarkentin/Desktop")

df = pd.read_csv('datahw4.csv', header=[0,1], skip_blank_lines = True)
array = df.dropna()

## Constants ##
fuck = 5.7e9

##Plot 1 ##
rho1 = array.iloc[:,0]
Penis = fuck * (10 ** rho1)**(4/3)

## Slope thingy
p1 = np.polyfit(x= array.iloc[:,0], y = array.iloc[:, 1], deg =1)  
print("The fitted slope of the line is: ",p1)

plt.figure("one")
plt.plot(array.iloc[:,0],np.log10(Penis))
plt.plot(array.iloc[:, 0], array.iloc[:, 1]) 

## Plot 2 ##
rho2 = array.iloc[:,2]
Penis2 = fuck * (10 ** rho2)**(4/3)


p2 = np.polyfit(x= array.iloc[:,2], y = array.iloc[:, 3], deg =1)  
print("The fitted slope of the line is: ",p2)

plt.figure("two")
plt.plot(array.iloc[:, 2], array.iloc[:, 3])
plt.plot(array.iloc[:, 2], np.log10(Penis2))

rho3 = array.iloc[:,4]
Penis3 = fuck * (10 ** rho3)**(4/3)

p3 = np.polyfit(x= array.iloc[:,4], y = array.iloc[:, 5], deg =1)  
print("The fitted slope of the line is: ",p3)

plt.figure("three")
plt.plot(array.iloc[:, 4], array.iloc[:, 5])
plt.plot(array.iloc[:, 4], np.log10(Penis3))
plt.show()