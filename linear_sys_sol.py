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

    return np.array(matrix_sys), np.array(matrix_b)



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
    
    return np.array(incs)

a = [
    [1, 2, 3],
    [10, 20, 33],
    [9, 8, 7],
]

b = [
    [2, ],
    [3, ],
    [4, ],
]

print(cramer_lin_sol())