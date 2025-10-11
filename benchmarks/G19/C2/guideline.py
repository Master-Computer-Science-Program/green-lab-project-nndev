import math
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time


if __name__ == "__main__":
    start=time.time()
    looper=config.C2_ARG
    for i in looper:
        print((round(math.sqrt((i[0]**2) + (i[1]**2)), 2),round(math.degrees(math.atan2(i[1], i[0])), 2)))
    end=time.time()
    print(end-start)