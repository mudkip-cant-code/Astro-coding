import os
import matplotlib.pyplot as plt
import numpy as np
import csv

os.chdir("/Users/jonthanwarkentin/Desktop")

with open('rho-P_solar_model.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    numbers = []
    for row in spamreader:
        #print(', '.join(row))
        numbers.append(', '.join(row))
        
print(numbers)