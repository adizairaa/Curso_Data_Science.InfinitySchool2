# Você recebeu a lista de registros de notas registros = [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]. 
# Escreva um código que use um laço for com desempacotamento de tupla para calcular a média de todas as notas.
#  Imprima o nome do aluno com a maior nota.

maior = 0
nome = ''
notas_registros = [("João", 8.5), ("Maria", 9.0), ("Pedro", 7.5)]
soma = 0
for i in notas_registros:
    x, y = i  
    soma += y
    if y > maior: 
        maior = y 
        nome = x  
media =  soma /len(notas_registros) 
print(f'{media}')
print(f'{nome}')