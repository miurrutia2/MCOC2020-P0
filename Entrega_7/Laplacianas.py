import numpy as np
from scipy.sparse import lil_matrix, csc_matrix

def matriz_laplaciana_llena(N, dtype = np.double):
    A = np.identity(N, dtype) * 2
    for i in range(N):
        for j in range(N):
            if i + 1 == j or i == j + 1:
                A[i, j] = - 1

    return A      

def matriz_laplaciana_dispersa(N, dtype = np.double):
    A = lil_matrix((N,N))
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i, j] = 2
            if (i + 1) == j or (i - 1) == j: 
                A[i, j] = - 1      
    return csc_matrix(A)


               