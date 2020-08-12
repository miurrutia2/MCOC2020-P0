import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
from Laplaciana import L_half

N = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000, 5000]

#Este codigo no funciona debido a que np.linalg no soporta archivos tipo float16

for i in range(10):
    
    dts = []
    memory = []
    
    archivo = (f"inversa{i}.txt")
    
    fid = open(archivo, "w")
    
    for n in N:
        
        
        A = L_half(n)
        
        t1 = perf_counter()
    
        C = np.linalg.inv(A) 
    
        t2 = perf_counter()
    
        dt = t2 - t1
        
        size = 3 * (n**2) * 8
        
        dts.append(dt)
        memory.append(size)
        
        fid.write(F"{n} {dt} {size}\n")

        fid.flush()
    fid.close()

val1 = []
t1 = []
mem1 = []

for n in range(10):
    val = []
    t = []
    mem = []
    with open(f"inversa{n}.txt", "r") as f:
        lineas = [linea.split() for linea in f]
        
    for i in lineas:
        val.append(int(i[0]))
        t.append(float(i[1]))
        mem.append(int(i[2]))
    
    val1.append(val)
    t1.append(t)
    mem1.append(mem)
    





plt.subplot(2, 1, 1)

plt.plot(val1[0],t1[0],"-o", color = "red")
plt.plot(val1[0],t1[1],"-o", color = "sienna")
plt.plot(val1[0],t1[2],"-o", color = "gray")
plt.plot(val1[0],t1[3],"-o", color = "orange")
plt.plot(val1[0],t1[4],"-o", color = "royalblue")
plt.plot(val1[0],t1[5],"-o", color = "darkseagreen")
plt.plot(val1[0],t1[6],"-o", color = "y")
plt.plot(val1[0],t1[7],"-o", color = "violet")
plt.plot(val1[0],t1[8],"-o", color = "mediumpurple")
plt.plot(val1[0],t1[9],"-o", color = "darkturquoise")
plt.yscale('log')
plt.xscale('log')

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xticks_text = ["", "", "", "", "", "", "", "", "", "", ""]

yticks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
yticks_text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]

plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text)

plt.title("Rendimiento caso 1 half")
plt.ylabel("Tiempo transcurrido (s)")
plt.grid()


plt.subplot(2, 1, 2)

plt.plot(N,memory,'-ob')

plt.yscale('log')
plt.xscale('log')

xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
xticks_text = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

yticks = [1000,10000, 100000, 1000000, 10000000, 100000000, 1000000000, 100000000000]
yticks_text = ["1 KB ", "10 KB", "100 KB", "1 MB", "10 MB", "100 MB", "1 GB", "10 GB"]

plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text)

plt.xlabel("Tamaño matriz N")
plt.ylabel("Uso memoria (s)")
plt.grid()


plt.show()