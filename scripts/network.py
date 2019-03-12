#!/usr/bin/env python3
import sys
import time
import os 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

magic_time=0.997

rx_file=open("/sys/class/net/wlp3s0/statistics/rx_bytes")
tx_file=open("/sys/class/net/wlp3s0/statistics/tx_bytes")
tx_dropped_file=open("/sys/class/net/wlp3s0/statistics/tx_dropped")
rx_dropped_file=open("/sys/class/net/wlp3s0/statistics/rx_dropped")
collisons_file=open("/sys/class/net/wlp3s0/statistics/collisions")

rx_abs = rx_old = tx_abs = tx_old = tx_dropped = rx_dropped = collisons=0

prev_time = time.time()

def rx_readline():
    global rx_abs,rx_old
    rx_abs=int(rx_file.readline())
    ret=(rx_abs-rx_old)*8/1000
    rx_old=rx_abs
    rx_file.seek(0,0)
    return ret

def tx_readline():
    global tx_abs,tx_old
    tx_abs=int(tx_file.readline())
    ret=(tx_abs-tx_old)*8/1000
    tx_old=tx_abs
    tx_file.seek(0,0)
    return ret

def rx_dropped_readline():
    dropped=int(rx_dropped_file.readline())
    rx_dropped_file.seek(0,0)
    return dropped

def handle_time():
    global magic_time,prev_time
    time_m=time.time()
    diff=time_m-prev_time
    if diff < 1:
        magic_time+=0.005
    else:
        magic_time-=0.005
    prev_time=time_m
    #print("Difference: " + str(diff))    
    return

def print_interfaces(interfaces):
    sys.stdout.write( bcolors.WARNING + "Available Interfaces: " + bcolors.ENDC)
    for x in interfaces:
        sys.stdout.write(str(x)+" ")
    sys.stdout.write("\n")

while(1):
    os.system("clear")
    dirs = os.listdir("/sys/class/net")
    print_interfaces(dirs)
    print(bcolors.OKGREEN + "Down: " + bcolors.ENDC + str(rx_readline())[:4]+"kB/s")
    print(bcolors.OKBLUE + "Up: " + bcolors.ENDC  + str(tx_readline())[:4]+"kB/s")
    print(bcolors.FAIL + "Dropped: " + bcolors.ENDC + str(rx_dropped_readline()))
    handle_time()
    time.sleep(magic_time)
