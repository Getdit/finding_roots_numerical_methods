from math import *
from utils import *

from datetime import datetime

SHOW_ITERATIONS = False

def calcula(a, b, formula, e, counter=0):
    """
    This method finds the a root of f(x) between two points, using the False Position numerical method.

    :param a: Value of x-axis, before the signal invertion
    :param b: Value of x-axis, after the signal invertion
    :param e: Ideal error

    :return: The root or call itself in recursion
    """
    counter += 1

    # get the values of f(a) and f(b)
    f_a = execute_formula(formula, a)
    f_b  = execute_formula(formula, b)

    # use false position formual to calc next value of x
    x_ns = (a*f_b - b*f_a)/(f_b-f_a)
    
    # calc f(x_ns) and set the error as his module
    f_xns = execute_formula(formula, x_ns)
    real_e = abs(f_xns)

    # calc h1 and h2
    h1 = f_a * f_xns
    h2 = f_b * f_xns

    # print iterations
    if SHOW_ITERATIONS:
        print(f"  Iteração: {counter}  \n    |\n    |----> A: {round(a, 5)}  \n    |----> B: {round(b, 5)}  \n    |----> f(A): {round(f_a, 5)}  \n    |----> f(B): {round(f_b, 5)}  \n    |----> x_ns: {round(x_ns, 5)}  \n    |----> f(x_ns): {round(f_xns, 5)}  \n    |----> f(A)*f(x_ns): {round(h1, 5)}  \n    |----> f(x_ns)*f(B): {round(h2, 5)}  \n    |----> E ideal: {e}  \n    |----> E: {round(real_e, 9)}\n\n")

    # if error is <= of ideal error, finish
    if real_e <= e:
        if SHOW_ITERATIONS:
            print("FIM")

        return x_ns, counter

    # avaluate the new a or b value
    if (h1 < 0 and h2 >= 0):
        return calcula(a, x_ns, formula, e, counter)
    else:
        return calcula(x_ns, b, formula, e, counter)


print("Método da Falsa Posição")

# Get the input data
form = input("Insira a fórmula f(x) > ")
x_minus = int(input("Insira o ponto inicial > "))
x_plus = int(input("Insira o ponto final > "))

e_ideal = float(input("Insira o erro ideal > "))

SHOW_ITERATIONS = True if input("Mostrar iterações? S ou N (interessante para análises)").lower() == "s" else False

# get the points and inversions
points, inversions, found_roots = get_points(form, x_minus, x_plus)

time_sum = 0

# For each inversion, use the false positon method to calc the root
for a, b in inversions:
    # Get the ini time
    init_time = datetime.now()

    # use the false positon method and get the roor and steps o it
    r, steps= calcula(a, b, form, e_ideal)

    # Store found root in found_roots
    found_roots.append(r)

    #get end time
    end_time = datetime.now()

    # calc and print execution time
    duration = end_time-init_time
    time_sum += duration.total_seconds()
    print(f"Duração: {duration.total_seconds()}s\nPassos: {steps}\n\n")

print(f"Média das execuções do algorítmo: {time_sum/len(inversions)}s")

# plot the graph
plot_graphic(points, found_roots)
