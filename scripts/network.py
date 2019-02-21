#!/usr/bin/env python3
import sys
import time
import os 

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



while(1):
    os.system("clear")
    dirs = os.listdir("/sys/class/net")
    print("Available Interfaces: " + str(dirs))
    print("Down: " + str(rx_readline())+"kB/s")
    print("Up: " + str(tx_readline())+"kB/s")
    handle_time()
    time.sleep(magic_time)
