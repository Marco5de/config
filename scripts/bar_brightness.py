#!/usr/bin/env python3
import sys

MAX=7500

filename="/sys/class/backlight/intel_backlight/brightness"
file=open(filename,"r")
curr_abs=file.readline()
file.close()

rel=int(curr_abs)/MAX*100
print(str(rel)[:4] + "%")


