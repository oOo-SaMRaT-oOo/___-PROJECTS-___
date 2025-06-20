# Voltage simulation for each 10 sec

import numpy as np
import datetime as dt
from datetime import timedelta

start_time = dt.datetime.now()
voltage_array = np.random.uniform(210,225,size = 10)
time_stamp = []
j = 0 

for i in range(10):
    current_time = start_time + timedelta(seconds=j)
    j += 10
    time_stamp.append(current_time)

print("\nObservation data :")
for i in range(10):
    print(f"Time - {time_stamp[i].time()} ... Voltage - {voltage_array[i]:.2f} V")

print()
print("Statistical analysis :")
print("Max voltage :",np.max(voltage_array),"V")
print("Average voltage :",np.average(voltage_array),"V")
print("Mean voltage :",np.mean(voltage_array),"V")
print("Standard deviation :",np.std(voltage_array))
print()








