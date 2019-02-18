#!/usr/bin/env python3
import sys

filename="/sys/class/thermal/thermal_zone0/temp"
file=open(filename,"r")
curr_temp=int((file.readline()))/1000
file.close()

print(str(curr_temp) + "°C")
