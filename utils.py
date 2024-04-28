import matplotlib.pyplot as plt
from math import *

def execute_formula(f, x):
    """
    This function replace the value X in function, then execute it.
    :param f: String, function in x
    :param x: Float, The value of x
    :return: f(a) as float
    """
    return eval(f.replace("x", f"({x})"))

def get_points(formula, x_minus, x_plus, get_roots=False):
    """
    This function will get all discret points in a range [x_minus, x_plus]
    :param x_minus: The min value of x
    :param x_plus: The max value of x
    :return: The points as list<tuple<int, int>>, the inversion points as list<tuple<int, int>>, the found roots as list<int> (if get_roots = True)
    """
    points = []
    inversions = []
    found_roots = []

    signal_plus = None

    # Each value in the range [x_minus, x_plus], set x
    for x in range(x_minus, x_plus+1):
        # get the val as f(x)
        val = execute_formula(formula, str(x))

        # store the point
        points.append((x, val))
        
        if val > 0:
            if signal_plus == False:
                # if val is positive and the last value is negative, store the point as inversion
                inversions.append((x-1, x))

            # set signal_plus as val signal
            signal_plus = True
            
        elif val < 0:
            if signal_plus == True:
                # if val is negative and the last value is positive, store the point as inversion
                inversions.append((x-1, x))

            # set signal_plus as val signal
            signal_plus = False
        else:
            # set signal_plus as None
            signal_plus = None

            # if get_roots, store that root in found_roots. Else append as an invertion
            if get_roots:
                found_roots.append(x)
            else:
                inversions.append((x, x+1))

    return points, inversions, found_roots



def plot_graphic(points, roots):
    """
    This function usesmatplotlib to plot a graph by the points, an mark the roots
    :param points: list<tuple<int, int>>
    :param roots: list<int>
    :return:
    """
    x_l, y_l = [], []
    
    # split the points in two lists
    for p in points:
        x_l.append(p[0])
        y_l.append(p[1])

    # create the subplot
    fig, ax = plt.subplots()
    
    # plot the points
    ax.plot(x_l, y_l)

    # set the grid in background
    ax.grid()
    
    # plot roots
    for r in roots:
        ax.scatter(r, 0, )

    # show graph
    plt.show()
