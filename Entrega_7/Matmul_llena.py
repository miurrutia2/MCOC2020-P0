import matplotlib.pyplot as plt
import numpy as np


names = ["MATMUL_llena.txt"]
N = [2, 5, 10, 12, 15, 20, 30, 40, 50, 55, 60, 100, 125, 160, 200, 350, 500, 800, 1000, 5000, 8000]
    
xticks = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
yticks = [0.1/1000, 1/1000, 10/1000, 0.1, 1, 10, 60, 600]
yticks_text = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min"]
xticks_text = ["", "", "", "", "", "", "", "", "", "", ""]
plt.figure()

dt1max = []
dt2max = []
for i in names:
    data = np.loadtxt(i)
    Ns = data[:,0]
    dts1 =  data[:,1]
    dts2 = data[:, 2]
    Nsmax = max(Ns)
    dts1max = max(dts1)
    dts2max = max(dts2)
    
    for i in Ns:
        dt1max.append(max(dts1))
        dt2max.append(max(dts2))
        
    plt.subplot(2,1,1) 
    plt.ylabel("Tiempo de ensamblado")
    plt.loglog(Ns,dts1, 'k-o', alpha = 0.5, markersize = 3) 
    plt.grid()
    plt.yticks(yticks, yticks_text)
    plt.xticks(xticks, xticks_text, rotation=45)
    
    plt.subplot(2,1,2) 
    plt.loglog(Ns,dts2, 'k-o', alpha = 0.5, markersize = 3)
    plt.ylabel("Tiempo de solucion")
    plt.xlabel("Tamaño de la matriz")
    plt.grid()
    plt.yticks(yticks, yticks_text)
    plt.xticks(xticks, xticks, rotation=45)
    
plt.subplot(2,1,1)  
plt.plot(Ns, dt1max, "--", color = "royalblue")  
plt.loglog(Ns, Ns*(dts1max/Nsmax), "--", color = "orange") 
plt.loglog(Ns, (Ns**2)*(dts1max/(Nsmax**2)), "--", color = "green") 
plt.loglog(Ns, (Ns**3)*(dts1max/(Nsmax**3)), "--", color = "firebrick") 
plt.loglog(Ns, (Ns**4)*(dts1max/(Nsmax**4)), "--", color = "mediumpurple") 
plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks_text, rotation=45) 

plt.subplot(2,1,2)  
plt.plot(Ns, dt2max, "--", color = "royalblue")  
plt.loglog(Ns, Ns*(dts2max/Nsmax), "--", color = "orange") 
plt.loglog(Ns, (Ns**2)*(dts2max/(Nsmax**2)), "--", color = "green") 
plt.loglog(Ns, (Ns**3)*(dts2max/(Nsmax**3)), "--", color = "firebrick") 
plt.loglog(Ns, (Ns**4)*(dts2max/(Nsmax**4)), "--", color = "mediumpurple") 
plt.yticks(yticks, yticks_text)
plt.xticks(xticks, xticks, rotation=45)
    


plt.tight_layout()
plt.legend()
plt.show()
