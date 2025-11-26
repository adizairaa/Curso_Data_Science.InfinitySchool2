# Crie um módulo chamado calculos.py que contém duas funções: calcular_media(lista) e calcular_soma(lista).
# A primeira deve retornar a média dos números em uma lista e a segunda deve retornar a soma.
# Em outro arquivo, chamado main.py, importe as duas funções do módulo calculos.py. 
# Crie uma lista de números [10, 20, 30, 40] e use as funções importadas para imprimir a média e a soma da lista.

from calculos import calcular_media 
from calculos import calcular_soma

lista = [10, 20, 30 ,40]

print (f'{calcular_media(lista)}')
print (f'{calcular_soma(lista)}')