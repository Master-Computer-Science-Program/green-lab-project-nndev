import string

C1_ARG = [[[i, i+1, i+2], i+3] for i in range(1, 300000)] #Elapsed time: 38.98418426513672 seconds
C2_ARG = [55] #Elapsed time: 30.849018096923828 seconds
C3_ARG = [i for i in range(40)] #Elapsed time: 27.026596307754517 seconds
C4_ARG = [i for i in range(35)] #Elapsed time: 28.851619482040405 seconds
C5_ARG = [[j for j in range(i * 10 + 1, i * 10 + 11)] for i in range(250000)] #Elapsed time: 27.230534315109253 seconds 
C6_ARG = [str(i) for i in range(100000)] #Elapsed time: 24.837823629379272 seconds
C7_ARG = [[[i, i+1, i+2, i+3], i+2] for i in range(1, 15000)]#Elapsed time: 38.39557123184204 seconds
C8_ARG = [["".join([chr((i + j) % 26 + 97) for j in range(9)]), [chr((i + k) % 26 + 97) + chr((i + k + 1) % 26 + 97) + chr((i + k + 2) % 26 + 97) for k in range(6)]] for i in range(0, 500000,2)]#Elapsed Time: 30.87672758102417 seconds
C9_ARG = [list(range(0, i)) + list(range(i-2, -1, -1)) for i in range(5, 25)] #Elapsed time: 40.16234993934631 seconds
C10_ARG = [[j for j in range(i, i + 5)] for i in range(1, 1000001, 4)] #Elapsed time: 30.4822359085083 seconds