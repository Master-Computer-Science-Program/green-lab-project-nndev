"""Convert between different units of temperature"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

if __name__ == "__main__":
    start=time.time()
    looper=config.C10_ARG
    for i in looper:
        print(round((float(i[0]) - 491.67) * 5 / 9, i[1])) #Rankine to celsius
        print(round(float(i[0]) - 459.67, i[1]))#Rankine to Farenheit
        print(round((float(i[0]) * 5 / 9), i[1]))#Rankine to Kelvin
        print(round((float(i[0]) * 1.25), i[1]))#Reaumr to Celsius
        print(round((float(i[0]) * 2.25 + 32), i[1]))#Reaumur to Farenheit
        print(round((float(i[0]) * 1.25 + 273.15), i[1])) #Reaumur to Kelvin
        print(round((float(i[0]) * 2.25 + 32 + 459.67), i[1]))#Reaumur to Rankine
        print(round((float(i[0]) * 9 / 5) + 32, i[1]))#celsius to farenheit
        print(round(float(i[0]) + 273.15, i[1])) #celsius to Kelvin
        print(round((float(i[0]) * 9 / 5) + 491.67, i[1]))#celsius to rankine
        print(round((float(i[0]) - 32) * 5 / 9, i[1]))#farenheit to celsius
        print(round(((float(i[0]) - 32) * 5 / 9) + 273.15, i[1]))#Farenheit to Kelvin
        print(round(float(i[0]) + 459.67, i[1]))#Farenheit to rankine
        print(round(float(i[0]) - 273.15, i[1]))#Kelvin to celsius
        print(round(((float(i[0]) - 273.15) * 9 / 5) + 32, i[1]))#Kelvin to farenheit
        print(round((float(i[0]) * 9 / 5), i[1]))#Kelvin to Rankine
    end=time.time()
    print(end-start)