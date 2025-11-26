# Você recebeu a lista de notas notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]. 
# Escreva um código que use um laço for para calcular a média de todas as notas. 
# Use uma list comprehension para criar uma nova lista  chamada notas_aprovados contendo apenas as notas que são maiores ou iguais a 7.0.
#  Imprima a média e a lista de notas dos aprovados.

notas_brutas = [8.5, 9.0, 7.5, 8.0, 6.5, 9.0, 10.0, 5.0, 8.5]
soma = 0 
for i in notas_brutas:
    soma += i
media =  soma/len(notas_brutas)
notas_aprovados = [ n for n in notas_brutas if n >= 7.0]
print(f'{notas_aprovados}')