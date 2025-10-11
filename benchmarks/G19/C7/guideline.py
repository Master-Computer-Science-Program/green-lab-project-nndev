import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

if __name__ == "__main__":
    start=time.time()
    looper=config.C7_ARG
    for i in looper:
        print(int((i[0], i[1]).count(1) != 0))
    end=time.time()
    print(end-start)
