from linear_sys_sol import cramer_lin_sol
import numpy as np

def adjust_lin_func(points):
    sum_xi = 0
    sum_fxi = 0
    sum_xi2 = 0
    sum_xi_fxi = 0

    m = len(points)

    for x, y in points:
        sum_xi += x
        sum_fxi += y
        sum_xi2 += x**2
        sum_xi_fxi += x*y

    a = np.array([
        [m, sum_xi],
        [sum_xi, sum_xi2],
    ], dtype=float)

    b = np.array([
        [sum_fxi], [sum_xi_fxi]
    ], dtype=float)

    sol = cramer_lin_sol(a, b)
    
    return lambda x: sol[0] + sol[1] * x
