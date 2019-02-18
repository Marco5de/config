#!/usr/bin/env python3
import sys

filename="/proc/meminfo"
file=open(filename,"r")
for x in range(4):
    next(file)
   
buffered=file.readline()
buffered = [int(s) for s in buffered.split() if s.isdigit()]
print(str(buffered[0]/1000000)[:4] + "GB")
