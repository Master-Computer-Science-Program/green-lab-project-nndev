import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config 
import time

if __name__ == "__main__":
    start=time.time()
    looper=config.C7_ARG
    for i in looper:
        if(len(i)==2):
            print(int(i[0] and i[1]))
        else:
            print (int(all(i) ))
    end=time.time()
    print(end-start)
