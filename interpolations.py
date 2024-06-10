from linear_sys_sol import cramer_lin_sol
import numpy as np
from math import pi

def get_linear_interpolation_function(x0, y0, x1, y1):
    a = np.array([
        [x0, 1],
        [x1, 1]
    ], dtype=float)

    b = np.array([
        [y0], [y1]
    ], dtype=float)

    sol = cramer_lin_sol(a, b)
    return lambda x: sol[0]*x + sol[1]

def get_quadratic_interpolation_function(x0, y0, x1, y1, x2, y2):
    a = np.array([
        [x0**2, x0, 1],
        [x1**2, x1, 1],
        [x2**2, x2, 1],
    ], dtype=float)

    b = np.array([
        [y0], [y1], [y2]
    ], dtype=float)

    sol = cramer_lin_sol(a, b)
    print(sol)
    return lambda x: sol[0]*(x**2) + sol[1]*x + sol[2]
