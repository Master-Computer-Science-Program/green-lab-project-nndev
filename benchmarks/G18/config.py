import random
import string
C1_ARG = ([1, 2, 3], 20000)
C2_ARG = [200000] #Elapsed time: 30.849018096923828 seconds
C3_ARG = [i for i in range(10000)] #Elapsed time: 27.026596307754517 seconds
C4_ARG = [i for i in range(15000)] #Elapsed time: 28.851619482040405 seconds
C5_ARG = [[random.randint(1, 100) for _ in range(random.randint(1, 30))] for _ in range(100000)] #Elapsed time: 27.666810274124146 seconds 
C6_ARG = [str(i) for i in range(100000)] #Elapsed time: 24.837823629379272 seconds
C7_ARG = [[i for i in range(80000)],8000] #Elapsed time : 29.63645315170288 seconds no_guideline issue
#C8_ARG = []
C9_ARG = [[random.randint(1, 100) for _ in range(random.randint(3, 20))] for _ in range(90000)] #Elapsed time: 31.835820198059082 seconds
C10_ARG = [[random.randint(1, 100) for _ in range(random.randint(3, 20))] for _ in range(900)] #Elapsed time: 29.53456997871399 seconds