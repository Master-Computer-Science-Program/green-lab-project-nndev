import random
C1_ARG = [10000000] # Elapsed time: 35.4880268573761 seconds
C2_ARG = [[i, i] for i in range(250000)] #Elapsed time: 37.22756814956665 seconds
C3_ARG = [[i % 2] for i in range(60000)] #Elapsed time: 31.27198886871338 seconds
C4_ARG = [20000,1000,1234] # Elapsed time: 36.524689 seconds
C5_ARG = [20] #Elapsed time: 42.173985719680786 seconds
C6_ARG = [[i % 2, (i + 1) % 2] for i in range(70000)] #Elapsed time: 49.573535203933716 seconds
C7_ARG = [[(i + j) % 2 for j in range(2 + (i % 3))] for i in range(100000)] #Elapsed time: 31.265428066253662 seconds
C8_ARG = [('-' if i % 2 == 0 else '') + ''.join('01'[(j + i) % 2] for j in range(3 + (i % 6))) for i in range(50000)]#Elapsed time: 47.97943735122681 seconds
C9_ARG = [('-' if i % 2 == 0 else '') + str(i % 1_000_000) for i in range(100000)]#Elapsed time: 49.901254653930664 seconds
C10_ARG = [[float(i), 1] for i in range(25000)] #Elapsed time: 44.227471590042114 seconds