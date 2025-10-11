import random
C1_ARG = [10000000] # Elapsed time: 35.4880268573761 seconds
#C2_ARG = []
C3_ARG = [[random.randint(0,1) for _ in range(1)] for _ in range(150000)] #Elapsed time: 38.83473181724548 seconds
C4_ARG = [20000,1000,1234] # Elapsed time: 36.524689 seconds
C5_ARG = [20] #Elapsed time: 42.173985719680786 seconds
C6_ARG = [[random.randint(0,1) for _ in range(2)] for _ in range(150000)] #Elapsed time: 26.18706178665161 seconds
C7_ARG = [[random.randint(0,1) for _ in range(2,5)] for _ in range(100000)] #Elapsed time: 30.650795698165894 seconds
C8_ARG = [random.choice(['', '-']) + ''.join(random.choices(['0', '1'], k=random.randint(3, 8))) for _ in range(100000)] #Elapsed time: 33.675718784332275 seconds
C9_ARG = [str(random.choice(['', '-'])) + str(random.randint(0, 999999)) for _ in range(150000)] #Elapsed time: 30.262940883636475 seconds
C10_ARG = [[i, 1] for i in range(25000)] #Elapsed time: 44.227471590042114 seconds