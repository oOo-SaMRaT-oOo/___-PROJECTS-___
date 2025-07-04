# VOLTAGE CURRENT SIMULATION FOR PURE R,L and C

import numpy as np
import matplotlib.pyplot as plt
import math as m
import random as r

print("\n--- WELCOME TO RLC SIMULATION ---")

while True :

    print("\n--- PLEASE ENTER THE GIVEN DATA ---\n")
    print("\nFor individual simulation of passive components, give your option : ")
    print(f"\n+------------+----------+")
    print(f"|{' Options':12}|{' Choice':10}|")
    print(f"+------------+----------+")
    print(f"|{' Resistor':12}|{'  1.':10}|")
    print(f"+------------+----------+")
    print(f"|{' Capacitor':12}|{'  2.':10}|")
    print(f"+------------+----------+")
    print(f"|{' Inductor':12}|{'  3.':10}|")
    print(f"+------------+----------+\n")

    while True :
        choice = int(input("Enter your choice : "))
        if choice < 1 or choice > 3:
            print("--- INVALID CHOICE ---")
            print("--- PLEASE RE-ENTER ---")
            continue
        break

    max_voltage = int(input("Enter max value of voltage(V) : "))
    time_period = int(input("Enter time period(s) : "))
    angular_frequency = (2 * m.pi)/time_period
    time_array = np.arange(0,100)

    # For resistor

    if choice == 1:

        resistance = int(input("Enter value of resistance(ohm) : "))
        value_array_current_resistor = []
        value_array_voltage_resistor = []
        max_current_resistor = round(max_voltage/resistance,3)


        for i in range(100):
            value_array_current_resistor.append(max_current_resistor * np.sin(angular_frequency*time_array[i]))
            value_array_voltage_resistor.append(max_voltage * np.sin(angular_frequency*time_array[i]))

        rms_current_resistor = max_current_resistor/m.sqrt(2)
        mean_current_resistor = (2/m.pi)*max_current_resistor
        rms_voltage_resistor = max_voltage/m.sqrt(2)
        mean_voltage_resistor = (2/m.pi)*max_voltage

        fig,axs = plt.subplots(1,2)
        fig.suptitle("... CURRENT AND VOLTAGE IN RESISTOR ...",fontsize = 20)
        axs[0].plot(value_array_current_resistor)
        axs[0].set_title("Current")
        axs[0].grid(True)
        axs[0].set_xlabel("Time in 's'")
        axs[0].set_ylabel("Current in 'A'")
        axs[0].axhline(max_current_resistor,color="r",ls="--",label ="MAX")
        axs[0].axhline(rms_current_resistor,color="b",ls="--",label ="RMS")
        axs[0].axhline(mean_current_resistor,color="g",ls="--",label ="MEAN")
        axs[0].legend(loc="lower right")

        axs[1].plot(value_array_voltage_resistor)
        axs[1].set_title("Voltage")
        axs[1].grid(True)
        axs[1].set_xlabel("Time in 's'")
        axs[1].set_ylabel("Voltage in 'V'")
        axs[1].axhline(max_voltage,color="r",ls="--",label ="MAX")
        axs[1].axhline(rms_voltage_resistor,color="b",ls="--",label ="RMS")
        axs[1].axhline(mean_voltage_resistor,color="g",ls="--",label ="MEAN")
        axs[1].legend(loc="lower right")

        plt.tight_layout()
        plt.show()


    # For inductor 

    if choice == 3:
        inductance = int(input("Enter value of inductance(H) : "))
        inductive_reactance = inductance * angular_frequency
        max_current_inductor = round(max_voltage / inductive_reactance,3)
        value_array_current_inductor = []
        value_array_voltage_inductor = []

        for i in range(100):
            value_array_current_inductor.append(max_current_inductor * m.sin((angular_frequency*time_array[i])-m.radians(90)))
            value_array_voltage_inductor.append(max_voltage * m.sin((angular_frequency*time_array[i])))

        rms_current_inductor = max_current_inductor/m.sqrt(2)
        mean_current_inductor = (2/m.pi)*max_current_inductor
        rms_voltage_inductor = max_voltage/m.sqrt(2)
        mean_voltage_inductor = (2/m.pi)*max_voltage

        fig,axs = plt.subplots(1,2)
        fig.suptitle("... CURRENT AND VOLTAGE IN INDUCTOR ...",fontsize = 20)
        axs[0].plot(value_array_current_inductor)
        axs[0].set_title("Current")
        axs[0].grid(True)
        axs[0].set_xlabel("Time in 's'")
        axs[0].set_ylabel("Current in 'A'")
        axs[0].axhline(max_current_inductor,color="r",ls="--",label ="MAX")
        axs[0].axhline(rms_current_inductor,color="b",ls="--",label ="RMS")
        axs[0].axhline(mean_current_inductor,color="g",ls="--",label ="MEAN")
        axs[0].legend(loc="lower right")

        axs[1].plot(value_array_voltage_inductor)
        axs[1].set_title("Voltage")
        axs[1].grid(True)
        axs[1].set_xlabel("Time in 's'")
        axs[1].set_ylabel("Voltage in 'V'")
        axs[1].axhline(max_voltage,color="r",ls="--",label ="MAX")
        axs[1].axhline(rms_voltage_inductor,color="b",ls="--",label ="RMS")
        axs[1].axhline(mean_voltage_inductor,color="g",ls="--",label ="MEAN")
        axs[1].legend(loc="lower right")

        plt.tight_layout()
        plt.show()


    # For capacitor 

    if choice == 2:

        capacitance = int(input("Enter the value of capacitance (F) : "))
        capacitive_reactance = round(1/(angular_frequency*capacitance),3)
        max_current_capacitor = max_voltage / capacitive_reactance
        value_array_current_capacitor = []
        value_array_voltage_capacitor = []

        for i in range(100):
            value_array_current_capacitor.append(max_current_capacitor*m.sin((angular_frequency*time_array[i])+m.radians(90)))
            value_array_voltage_capacitor.append(max_voltage*m.sin((angular_frequency*time_array[i])))

        rms_current_capacitor = max_current_capacitor / m.sqrt(2)
        rms_voltage_capacitor = max_voltage / m.sqrt(2)
        mean_current_capacitor = (2/m.pi) * max_current_capacitor
        mean_voltage_capacitor = (2/m.pi) * max_voltage

        fig,axs = plt.subplots(1,2)
        fig.suptitle("... CURRENT AND VOLTAGE IN CAPACITOR ...",fontsize = 20)

        axs[0].plot(value_array_current_capacitor)
        axs[0].grid("True")
        axs[0].set_title("Current")
        axs[0].set_xlabel("Time in 's'")
        axs[0].set_ylabel("Current in 'A'")
        axs[0].axhline(max_current_capacitor,color = "red",ls="--",label = "MAX")
        axs[0].axhline(rms_current_capacitor,color = "b",ls="--",label = "RMS")
        axs[0].axhline(mean_current_capacitor,color = "g",ls="--",label = "MEAN")
        axs[0].legend(loc="lower right")

        axs[1].plot(value_array_voltage_capacitor)
        axs[1].grid("True")
        axs[1].set_title("Voltage")
        axs[1].set_xlabel("Time in 's'")
        axs[1].set_ylabel("Voltage in 'V'")
        axs[1].axhline(max_voltage,color = "red",ls="--",label = "MAX")
        axs[1].axhline(rms_voltage_capacitor,color = "b",ls="--",label = "RMS")
        axs[1].axhline(mean_voltage_capacitor,color = "g",ls="--",label = "MEAN")
        axs[1].legend(loc="lower right")

        plt.tight_layout()
        plt.show()

    print("\n--- DEAR USER, ENTER YOUR CHOICE ---")
    print(f"\n+------------+----------+")
    print(f"|{' Options':12}|{' Choice':10}|")
    print(f"+------------+----------+")
    print(f"|{' RE-START':12}|{'  1.':10}|")
    print(f"+------------+----------+")
    print(f"|{' EXIT':12}|{'  2.':10}|")
    print(f"+------------+----------+\n")

    while True :
        choice = int(input("Enter your choice : "))
        if choice !=1 and choice !=2:
            print("--- INVALID CHOICE ---")
            print("--- PLEASE RE-ENTER ---")
            continue
        break

    if choice == 2:
        print("--- THANK YOU USER ---")
        print("... EXITING ...")
        print("<3 :) <3")
        print()
        exit()


