from math import *
from utils import *

from datetime import datetime

SHOW_ITERATIONS = False


def calcula(xi, xi1, formula, e, counter=0):
    """
    This method try to find a root by two points, using the secant method
    """
    counter += 1

    # get a third point
    xi2 = xi1 - execute_formula(formula, xi1)*(xi-xi1)/(execute_formula(formula, xi) - execute_formula(formula, xi1))

    # if the third point is infinit, finish
    if xi2 == inf:
        print("Não foi possível estimar")
        return
    
    # verifi what poit is closer to the third
    if abs(xi -xi2) < abs(xi1 - xi2):
        xn = xi
    else:
        xn = xi1

    # get the error
    error = abs(xn - xi2)

    # print iteration
    if SHOW_ITERATIONS:
        print(f"  Iteração {counter}:\n        |\n        |----> x{counter-1}: {round(xi, 5)}\n        |----> x{counter}: {round(xi1, 5)}\n        |----> x{counter+1}: {round(xi2, 5)}\n        |----> erro estimado: {e}\n        |----> erro: {round(error, 9)}\n\n")

    # if error <= ideal error, finsh
    if error <= e:
        print("FIM")
        return xn, counter
    return calcula(xn, xi2, formula, e, counter)


print("Método da Secante")

# get the input data
form = input("Insira a fórmula f(x) > ")
x_minus = int(input("Insira o ponto inicial > "))
x_plus = int(input("Insira o ponto final > "))

e = float(input("insita o erro estimado > "))

SHOW_ITERATIONS = True if input("Mostrar iterações? S ou N (interessante para análises)").lower() == "s" else False

# get the points  and inversions
points, inversions, found_roots = get_points(form, x_minus, x_plus)

time_sum = 0

# for echar inversion, calc the root by the secant method
for a, b in inversions:
    # get the initial time
    init_time = datetime.now()

    # get the roor and steps
    r, steps= calcula(a, b, form, e)

    # store the found root to dound_roots
    found_roots.append(r)

    # get the end time
    end_time = datetime.now()

    # calculate and print the total time
    duration = end_time-init_time
    time_sum += duration.total_seconds()
    print(f"Duração: {duration.total_seconds()}s\nPassos: {steps}\n\n")

print(f"Média das execuções do algorítmo: {time_sum/len(inversions)}s")

# plot the graph
plot_graphic(points, found_roots)