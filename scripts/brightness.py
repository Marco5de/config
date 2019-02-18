#!/usr/bin/env python3
import sys

if(len(sys.argv)!=2):
    print("Usage: " + sys.argv[0] +" [+/-brightness]")
    sys.exit()


MIN=500
MAX=7500
curr_abs=0
curr_rel=0


filename="/sys/class/backlight/intel_backlight/brightness"
file=open(filename,"r")
for line in file:
    curr_abs=int(line)

curr_rel=curr_abs/MAX*100
file.close()

u_input = int(sys.argv[1][1:])*7500/100
if(sys.argv[1][0] == '+'):
    new_abs=curr_abs+u_input 
elif(sys.argv[1][0] == '-'):
    new_abs=curr_abs-u_input
else:
    print("Usage: brightness [+/-:brigthness]")
    sys.exit()

if(not(new_abs >= MIN and new_abs <= MAX)):
    print("Argument too large: brightness has to be between 500 and 7500 abs")
    if(new_abs<MIN):
        new_abs=MIN
    if(new_abs>MAX):
        new_abs=MAX

new_rel = new_abs/MAX*100
print("Brightness: " + str(new_rel))

n_file=open(filename,"w")
n_file.write('%d' % new_abs)
n_file.close()

