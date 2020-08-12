import numpy as np

def L_half(n):
    A = np.zeros([n,n], dtype = np.half)
    for i in range(n) :
        for j in range(n) :
            if i == j :
                A[i][j] = 2
            elif i == (j+1) or j == (i+1):
                A[i][j] = -1
    return A


def L_single(n):
    A = np.zeros([n,n], dtype = np.single)
    for i in range(n) :
        for j in range(n) :
            if i == j :
                A[i][j] = 2
            elif i == (j+1) or j == (i+1):
                A[i][j] = -1
    return A

def L_double(n):
    A = np.zeros([n,n], dtype = np.double)
    for i in range(n) :
        for j in range(n) :
            if i == j :
                A[i][j] = 2
            elif i == (j+1) or j == (i+1):
                A[i][j] = -1
    return A

def L_longdouble(n):
    A = np.zeros([n,n], dtype = np.longdouble)
    for i in range(n) :
        for j in range(n) :
            if i == j :
                A[i][j] = 2
            elif i == (j+1) or j == (i+1):
                A[i][j] = -1
    return A
