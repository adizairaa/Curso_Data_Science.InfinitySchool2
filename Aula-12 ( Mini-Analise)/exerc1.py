# Crie um script Python que leia o arquivo dados_simples.csv. Para cada linha de dados (ignorando o cabeçalho), você deve: Separar a linha nos seus três campos. Converter o campo Idade para inteiro (int). Converter o campo Altura_Metros para ponto flutuante (float). 
# Imprima o nome da pessoa e, na frente, a soma da sua Idade com sua Altura. Ex: Ana: 26.65.

import csv 
arquivo = open('dados_simples.csv', 'w')
dados = [
    ['nome', 'idade', 'altura'],
    ['Alex', '48', '1.81'],
    ['Adila', '21', '1.65'],
    ['Nathalia', '23', '1.69']
]
with open('dados_simples.csv', 'w', newline='') as d:
    writer = csv.writer (d , delimiter =",")
    writer.writerows(dados)
    
print("Arquivo'dados_simples.csv")

with open('dados_simples.csv', 'r', newline='') as d:
    inf= csv.reader(d, delimiter=',')
    next(inf)
    for lista in inf:
        nome = lista[0]
        idade = int(lista[1])
        altura = float(lista[2])
        print(f'{nome}, {altura+ idade}')