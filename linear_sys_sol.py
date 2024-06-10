import numpy as np

def input_linear_sys():
    sys_n = int(input("Insira o número de sistemas lineares: "))
    n_coefs = int(input("Insira o número máximo coeficientes: "))
    
    matrix_sys = []
    matrix_b = []

    for sn in range(sys_n):
        sys = list(map(float, input(f"Sistema {sn+1}: ").split()))
        sys_coefs_diff = n_coefs - len(sys) +1 

        if sys_coefs_diff > 0:
            sys =sys[:-1] + [0] * sys_coefs_diff + [sys[-1]]


        matrix_sys.append(sys[:-1])
        matrix_b.append([sys[-1]])

    return np.array(matrix_sys, dtype=float), np.array(matrix_b, dtype=float)



def get_det(matrix):
    return np.linalg.det(matrix)
    

def cramer_lin_sol(a=None, b=None):
    if a is None and b is None:
        a, b = input_linear_sys()
        
    lines, cols = a.shape

    det_a = get_det(a)

    incs = []
    
    for ind in range(cols):
        cp = a.copy()

        cp[:, ind] = b[:, 0]

        det = get_det(cp)

        inc = round(det/det_a, 5)

        incs.append(inc)
    
    return np.array(incs, dtype=float)

def gauss_jacobi_lin_sol(a=None, b=None, error=0.5, inc=None):
    if a is None or b is None:
        a, b = input_linear_sys()
        
    lines, cols = a.shape

    if inc is None:
        inc = [0] * cols
    
    elif len(inc) != cols:
        raise ValueError("INC incompleto")

    max_error = error + 1
    interaction = 0
    while max_error >= error:
        interaction+= 1
        temp_inc = []
        e = []
        for col in range(cols):
            x = (1/a[col, col])*(b[col][0] - sum([((a[col, j]*inc[j]) if j != col else 0) for j in range(len(inc))]))
            e.append(abs(x-inc[col]))
            temp_inc.append(x)
        inc = temp_inc
        max_error = max(e)
    
    return inc, interaction

def gauss_seidel_lin_sol(a=None, b=None, error=0.5, inc=None):
    if a is None or b is None:
        a, b = input_linear_sys()
        
    lines, cols = a.shape

    if inc is None:
        inc = [0] * cols
    
    elif len(inc) != cols:
        raise ValueError("INC incompleto")

    max_error = error + 1
    interaction = 0
    while max_error >= error:
        interaction+= 1
        e = []
        for col in range(cols):
            x = (1/a[col, col])*(b[col][0] - sum([((a[col, j]*inc[j]) if j != col else 0) for j in range(len(inc))]))
            e.append(abs(x-inc[col]))
            inc[col] = x
        max_error = max(e)
    
    return inc, interaction
