#!/usr/bin/env python3
import sys
import time


filename="/sys/class/net/wlp3s0/statistics/rx_bytes"
file=open(filename,"r")

old=0

while(1):
    abs=int(file.readline())
    curr=(abs-old)*8/1000
    print(str(curr) + "kBytes/s")
    old=abs
    #setting filepointer to beginning of file
    file.seek(0,0)
    time.sleep(1)

