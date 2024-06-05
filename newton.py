from math import *
from utils import *

from datetime import datetime

SHOW_ITERATIONS = False


def calcula(xi, formula, d_formula, e, counter=0):
    """
    This method finds the a root of f(x) between two points, using the Newton numerical method.

    :param xi: Value of x-axis estimated
    :param formula: Formual f(x)
    :param derivate of formula: Formual f'(x)
    :param e: Estimated error

    :return: The root or call itself in recursion
    """
    counter += 1

    # finds the next x value by the newton method
    xi1 = xi - execute_formula(formula, xi)/execute_formula(d_formula, xi)

    # calculate the error by the module of difference between the points
    error = abs(xi1 - xi)

    # show iteration
    if SHOW_ITERATIONS:
        print(f"  Iteração {counter}:\n        |\n        |----> x{counter}: {round(xi, 5)}\n        |----> x{counter+1}: {round(xi1, 5)}\n        |----> f(x{counter+1}): {round(execute_formula(formula, xi1), 20)}\n        |----> erro estimado: {e}\n        |----> erro: {round(error, 9)}\n\n")

    # if error <= the ideal error, finish. Otherwise, call itself
    if error <= e:
        if SHOW_ITERATIONS:
            print("FIM")
        return xi1, counter
    return calcula(xi1, formula, d_formula, e, counter)


print("Método de Newton")

# get input data
form = input("Insira a fórmula f(x) > ")
d_formula = input("Insira a derivada da fórmula f'(x) > ")
x_minus = int(input("Insira o ponto inicial > "))
x_plus = int(input("Insira o ponto final > "))

e = float(input("insita o erro estimado > "))

SHOW_ITERATIONS = True if input("Mostrar iterações? S ou N (interessante para análises)").lower() == "s" else False

# get the points, and inversions values
points, inversions, found_roots = get_points(form, x_minus, x_plus)

time_sum = 0

for a, b in inversions:
    try:
        # get the inital time
        init_time = datetime.now()

        # get the root by the newton method and the steps count
        r, steps= calcula(a, form, d_formula, e)

        # store the root in found_roots
        found_roots.append(r)

        #get the end time
        end_time = datetime.now()

        # calc and print the duration
        duration = end_time-init_time
        time_sum += duration.total_seconds()
        print(f"Duração: {duration.total_seconds()}s\nPassos: {steps}\n\n")
    except ZeroDivisionError:
        print(f"Não foi possível estimar para o ponto ({a}, {b})")

print(f"Média das execuções do algorítmo: {time_sum/len(inversions)}s")

# plot he graph
plot_graphic(points, found_roots)
