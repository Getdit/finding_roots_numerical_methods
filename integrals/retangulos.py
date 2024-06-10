# Método dos retângulos
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

    Ela divide o intervalo dos dois numeros da integral definida e define quais são os pontos onde cada base dos retângulos começam e terminam.

    Após definir quais são os pontos dessas bases, ela pega o ponto médio de cada base num array

    Esse array, portanto, contem os x_i que devemos utilizar, e por conta disso é o nosso retorno da função

    :param a: intervalo menor da integral
    :param b: intervalo maior da integral
    :param n: quantidade de retângulos utilizados

    :return: Um array com todas as iterações de x_i que devem ser utilizadas
    '''
    interval = (b-a)/n
    interacoes = [a]
    for num in range(n): interacoes.append(interacoes[num]+interval)
    x_i = []
    for num in range(len(interacoes)):
        if num != 0: x_i.append((interacoes[num]+(interacoes[num-1]))/2)
    return x_i
        

print("Método dos retângulos")

# Get the input data
form = input("Insira a fórmula f(x) > ")
n = int(input("Insira o número de retangulos (N) > "))
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
    if mostrar_calculos == True: print(f'\n ----------------- ITERACAO {contador} -----------------\n x = {x} // f(x) = {execute_formula(form, x)}')
    #Calcula o valor de x_i na formula e soma ao total
    soma = soma + execute_formula(form, x)

#Pega a soma final de todos os x_i e multipilica pelo tamanho das bases dos triangulos
resultado = ((b - a)/n)*soma
print(f'\nRESULTADO FINAL: {resultado}')