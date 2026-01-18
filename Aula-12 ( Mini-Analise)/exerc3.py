# Crie um script Python que leia o arquivo registros_vendas.csv. Você deve encontrar e imprimir: O menor Preco_Unitario encontrado em todas as transações. O maior Preco_Unitario encontrado em todas as transações. Dica: Inicialize a variável do Mínimo com um valor muito alto (ou float('inf')) e a do Máximo com um valor muito baixo (ou float('-inf')). Foco de Programação: Implementação da lógica de min e max usando estruturas if de comparação e a técnica de inicialização com valores extremos para garantir que a primeira comparação seja sempre válida.

import csv
maximo= float ('-inf')
minimo = float ('inf')

dados = [
['Produto','Preco_Unitario','Unidades_Vendidas'],
['Caneta','2.50','10'],
['Caderno','15.00','5'],
['Lápis','1.20','12'],
['Borracha','0.90','20']
]

with open('registros_vendas.csv', 'w', newline='', encoding = 'utf-8' ) as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)

with open('registros_vendas.csv', newline = '' ,encoding= 'utf-8' ) as registro:
    leitor = csv.DictReader(registro)

    for item in leitor:
        preco_unit= float(item['Preco_Unitario'])
        if preco_unit < minimo:
            minimo=preco_unit
        if preco_unit > maximo:
            maximo = preco_unit
print(f'{minimo}')           
print(f'{maximo}')           

