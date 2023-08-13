import sys,time,random

def print_slow(str):
    for i in str + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.002)
    
    time.sleep(0.4)
