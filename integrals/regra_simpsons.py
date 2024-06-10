# Regra de Simpson
#
# Description: esse programa vai definir a solução de uma integral definida
#
# Author: João Marcos Moço Giraldi
# Github: https://github.com/joao-giraldi
#

from math import *
from datetime import datetime

from utils import *

def get_interacoes(a,b,n):
    '''
    Esse função vai definir quais são os valores de x_i que os nossos calculos devem assumir.

    Ela divide o intervalo entre os pontos que serão calculados e separa eles numa array

    Esse array, portanto, contem os x_i que devemos utilizar, e por conta disso é o nosso retorno da função

    :param a: intervalo menor da integral
    :param b: intervalo maior da integral
    :param n: quantidade de pontos utilizados

    :return: Um array com todas as iterações de x_i que devem ser utilizadas
    '''
    interval = (b-a)/n
    interacoes = [a]
    for num in range(n): interacoes.append(interacoes[num]+interval)
    return interacoes
        

print("Método da regra de Simpson")

# Get the input data
form = input("Insira a fórmula f(x) > ")
n = int(input("Insira o número de pontos (n) > "))
a = float(input("Insira o intervalo menor da integral (a) > "))
b = float(input("Insira o intervalo maior da integral (b) > "))
mostrar_calculos = True if input("Mostrar iterações? S ou N (interessante para análises) > ").lower() == "s" else False

soma = 0

#Define quais são os x_i que devem ser utilizados
x_i = get_interacoes(a,b,n)

if mostrar_calculos == True: print(f'\nVALORES DE x_i QUE SERÃO UTILIZADOS:\n{x_i}')
contador = 0
for x in x_i: 
    contador = contador + 1
    #Calcula o valor de x_i na formula e soma ao total, usando a definição de constante aplicada no método da regra de simpson
    if contador == 1 or contador == len(x_i): resultado = (execute_formula(form, x))
    elif contador%2 == 1: resultado = 2*execute_formula(form, x)
    elif contador%2 == 0: resultado = 4*execute_formula(form, x)
    soma = soma + resultado
    if mostrar_calculos == True: print(f'\n ----------------- ITERACAO {contador-1} -----------------\n x = {round(x,3)} // f(x) = {resultado}')
    
#Pega a soma final de todos os x_i e multipilica pelo tamanho das bases dos triangulos
resultado = (((b - a)/n)/3)*soma
print(f'\nRESULTADO FINAL: {resultado}')
