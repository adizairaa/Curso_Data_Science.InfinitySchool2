# Análise de Vendas de Produtos Baratos Você é um analista de dados e precisa saber o total de faturamento gerado apenas pelos produtos considerados de baixo valor (aqueles com preço unitário menor ou igual a 100). Seu relatório final deve ser simples: deve conter a soma total do faturamento gerado por esses produtos baratos e a quantidade total de itens (unidades) vendidos nessa categoria. Instruções do Projeto: Reutilize o Código Base: Use a estrutura de leitura do arquivo vendas_ficticias.csv (criado no Slide 1) e a lógica de conversão de tipos (float e int) que você aprendeu. Variáveis de Agregação: Crie duas variáveis para acumular os resultados: faturamento_baixo_valor (inicializada em 0.0) e itens_vendidos_baixo_valor (inicializada em 0). 
# Filtro Condicional: Dentro do loop de leitura, adicione um comando if para processar a linha somente se o valor_unitario do produto for menor ou igual a 100.00. Cálculo e Acumulação: Dentro do bloco if (ou seja, se o produto for de baixo valor):
#  Calcule o faturamento da linha (valor_unitario x quantidade). Acumule este faturamento na variável faturamento_baixo_valor. Acumule a quantidade vendida na variável itens_vendidos_baixo_valor. 
# Exibição: Ao final, imprima o valor total acumulado em faturamento_baixo_valor e o total de itens_vendidos_baixo_valor. Siga o seguinte conteúdo(código) para criar o arquivo. 

import csv
NOME_ARQUIVO = 'vendas_ficticias.csv'

faturamento_baixo_valor = 0.0
itens_vendidos_baixo_valor = 0

dados = [
    ['Produto', 'Valor', 'Quantidade'],
    ['Celular', '1200.50', '2'],
    ['Notebook', '3500.00', '1'],
    ['Fone', '150.99', '5'],
    ['Mouse', '50.00', '3'],
    ['Teclado', '120', '2']
]
with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(dados)

with open(NOME_ARQUIVO, 'r', encoding='utf-8') as registro:
    leitor = csv.DictReader(registro)

    for linha in leitor:
        produto = linha ['Produto']
        valor = float(linha['Valor'])
        quantidade = int(linha['Quantidade'])

        if valor <= 100.00:
            faturamento_baixo_valor=valor*quantidade
            itens_vendidos_baixo_valor+=quantidade

print(f'Faturamento {faturamento_baixo_valor}')
print(f'Quantidade {itens_vendidos_baixo_valor}')

