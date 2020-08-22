import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
from time import perf_counter


N = [2, 5]


def matriz_laplaciana_llena(N, dtype = np.double):
    A = np.identity(N, dtype)*2-np.eye(N,k=-1)-np.eye(N,k=1)
    return A


names = ["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symmetric.txt", "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"]

files = [open(name, "w") for name in names]

for i in N:
    
    dts = np.zeros((5, len(files)))
    print(f"N = {i}")
    A = matriz_laplaciana(i)
    B = np.ones(i)

    for n in range(5):
        
        #Invertir matriz
        t1 = perf_counter()
        inv_A = np.linalg.inv(A)      
        inv = inv_A@B
        t2 = perf_counter()
        
        dt1 = t2 - t1
        
        dts[n][0] = dt1
        #
        
        #Usando solve np
        t1 = perf_counter() 
        np.linalg.solve(A,B)
        t2 = perf_counter()
        
        dt2 = t2 - t1
        
        dts[n][1] = dt2
        #
        
        #Usando solve scipy
        t1 = perf_counter() 
        linalg.solve(A,B)
        t2 = perf_counter()
        
        dt3 = t2 - t1
        
        dts[n][2] = dt3
        #
        
        #Usando solve scipy symmetry
        t1 = perf_counter() 
        linalg.solve(A,B, assume_a = "sym" )
        t2 = perf_counter()
        
        dt3 = t2 - t1
        
        dts[n][3] = dt3
        #
        
        #Usando solve scipy pos
        t1 = perf_counter() 
        linalg.solve(A,B, assume_a = "pos" )
        t2 = perf_counter()
        
        dt3 = t2 - t1
        
        dts[n][4] = dt3
        #
        
        #Usando solve scipy pos overwrite
        t1 = perf_counter() 
        linalg.solve(A,B, assume_a = "pos", overwrite_a=True, overwrite_b=True )
        t2 = perf_counter()
        
        dt3 = t2 - t1
        
        dts[n][5] = dt3
        #
        
        
    print ("dts: ", dts)
    
    dts_mean = [np.mean(dts[:,j]) for j in range(len(files))]
    
    print("dts_mean : ", dts_mean)
    
    for j in range(len(files)):
        files[j].write(f"{i} {dts_mean[j]}\n")
        files[j].flush()
        
[file.close() for file in files]
        

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
yticks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
yticks_text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

plt.figure()

for i in names:
    data = np.loadtxt(i)
    Ns = data[:,0]
    dts =  data[:,1]
    
    print("Ns: ", Ns)
    print("dts: ", dts)
    plt.grid(b = True)
    plt.loglog(Ns, dts.T, "-o", label = i)
    plt.ylabel("Tiempo transcurrido (s)")
    plt.xlabel("Tamaño de la matriz")
    
    plt.yticks(yticks, yticks_text)
    plt.xticks(xticks, xticks, rotation=45)
    
plt.tight_layout()
plt.legend()
plt.show()
    
    
