# Voltage simulation in House_Hold

import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from datetime import timedelta

voltage_array = np.random.uniform(220,223,size = 10)
start_time = dt.datetime.now()
j = 0
time_stamp = []
time_stamp_time_only =[]

for i in range(10):
    current_time = start_time + timedelta(seconds=j)
    j += 1
    time_stamp.append(current_time)

print("\nObservation data :")
for i in range(10):
    print(f" Time : {time_stamp[i].time()} ~ Voltage : {voltage_array[i]:.2f} V ")
    time_stamp_time_only.append(time_stamp[i].strftime("%I:%M:%S~%p"))
print()
average_voltage = np.average(voltage_array)
max_voltage = np.max(voltage_array)
min_voltage = np.min(voltage_array)

# For visualization 

plt.plot(time_stamp_time_only,voltage_array,label = "voltage")
plt.axhline(average_voltage,color = "red",linestyle = "--",label = "Average Voltage")
plt.axhline(max_voltage,color = "black",linestyle = "--",label = "Maximum Voltage")
plt.axhline(min_voltage,color = "green",linestyle = "--",label = "Minimum Voltage")
plt.title("Voltage Simulation '(220-223)' V",fontsize = 25)
plt.xlabel("Time Axis")
plt.ylabel("Voltage in 'V'")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.xticks(rotation = 45)
plt.show()





