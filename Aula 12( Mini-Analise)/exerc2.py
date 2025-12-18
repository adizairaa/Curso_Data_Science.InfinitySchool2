# Crie um script Python que leia o arquivo registros_vendas.csv. Seu script deve calcular e imprimir: A soma total de Unidades_Vendidas (total de itens vendidos, independentemente do tipo). A contagem total de transações (número de linhas de dados válidas). O faturamento total gerado somente pelas vendas do item "Caneta".

import csv 
venda_alex = 0 
total_transacoes = 0 
soma_total_vendas = 0 

arquivo = open('registro_vendas.csv', 'w')
dados = [
    ['item', 'total_venda', 'unidades_ven'],
    ['Alex', '3', '32'],
    ['Adila', '7', '21'],
    ['Nathalia', '2', '3']
]


with open('registro_vendas.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)

with open ('registro_vendas.csv', newline ='',encoding="utf-8" ) as vendas:
    leitor =csv.DictReader(vendas)
    
    for mercadoria in leitor:
        produto = mercadoria['item']
        unidades = int( mercadoria ['total_venda'])
        venda = float(mercadoria['unidades_ven'])
        soma_total_vendas += venda
        total_transacoes += 1 

        if produto== 'Alex':
            venda_alex= unidades* venda

       

print(f'Total de vendas de Alex={venda_alex}')
print (f'{soma_total_vendas}')
print (f'{total_transacoes}')


