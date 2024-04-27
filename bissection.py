# Bissection Method
#
# Description: This program will try to find the roots of any equation by the numerical bissection method
#
# Author: Eduardo Chedid
# Github: https://github.com/Getdit
#


from math import *
from datetime import datetime

from utils import *


SHOW_ITERATIONS = False

def calc_k(a: float, b: float, e: float) -> int:
    """
    This method finds the k value for the bissection method. In other words, it will return the number of iterations that the method will need.

        log(b-a) - log(e)
    K = ------------------
              log(2)

    if K has decimal values, k gets the next integer.

    :param a: Value of x-axis, before the signal invertion
    :param b: Value of x-axis, after the signal invertion
    :param e: Ideal error

    :return: The K value. The number of iterations that the method will need
    """
    k = (log(b-a)-log(e))/log(2)
    k0 = int(k)

    return k0 if k == k0 else k0+1


def calcula(a, b, form, e_ideal, k_val, k = 0):
    """
    This method performs an iteration of the bisection method. If it doesn't find the result, it recursively calls itself.
    """
    # set the counter as k
    k = k+1 

    # the the median point between a and b
    xm = (a+b)/2
    
    # get f(a), f(b) and f(x), values
    f_a = execute_formula(form, a)
    f_b = execute_formula(form, b)
    f_x = execute_formula(form, xm)

    # print iterations
    if SHOW_ITERATIONS:
        print(f"    Iteração {k}:\n        |\n        |----> A: {round(a, 5)}\n        |----> B: {round(b, 5)}\n        |----> xm: {round(xm, 5)}\n        |----> f(xm): {round(f_x, 5)}\n\n")

    # if k reachs the k_val, finish
    if k == k_val:
        if SHOW_ITERATIONS:
            print("FIM")
        return xm
        
    # finds the next a or b point
    if f_a * f_x <= 0:
        return calcula(a, xm, form, e_ideal, k_val, k)

    elif f_b * f_x < 0:
        return calcula(xm, b, form, e_ideal, k_val, k)


print("Método da Bisseção")

# Get the input data
form = input("Insira a fórmula f(x) > ")
x_minus = int(input("Insira o ponto inicial > "))
x_plus = int(input("Insira o ponto final > "))

e_ideal = float(input("Insira o erro ideal > "))

SHOW_ITERATIONS = True if input("Mostrar iterações? S ou N (interessante para análises)").lower() == "s" else False

# get the points and inversions
points, inversions, found_roots = get_points(form, x_minus, x_plus)

time_sum = 0

# For each inversion, use the bissection method to calc the root
for a, b in inversions:
    # Get the ini time
    init_time = datetime.now()

    # Get the value  of K
    k_val = calc_k(a, b, e_ideal)

    # use the bissection method
    r = calcula(a, b, form, e_ideal, k_val)

    # Store found root in found_roots
    found_roots.append(r)

    #get end time
    end_time = datetime.now()

    # calc and print execution time
    duration = end_time-init_time
    time_sum += duration.total_seconds()
    print(f"Duração: {duration.total_seconds()}s\nPassos: {k_val}\n\n")

print(f"Média das execuções do algorítmo: {time_sum/len(inversions)}s")

# plot the graph
plot_graphic(points, found_roots)

