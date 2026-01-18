import csv

dados = [
    ["produto", "preco"],
    ["Camisa", 50],
    ["Calça", 120],
    ["Tênis", 300],
    ["Boné", 40],
    ["Moletom", 150]
]

# criando o arquivo
with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print("Arquivo vendas.csv criado com sucesso!")



with open("vendas.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)  # pular cabeçalho

    faturamento_total = 0
    count = 0

    produto_mais_caro = None
    preco_max = float('-inf')

    produto_mais_barato = None
    preco_min = float('inf')

    for linha in leitor:
        produto = linha[0]
        preco = float(linha[1])

        faturamento_total += preco
        count += 1

        
        if preco > preco_max:
            preco_max = preco
            produto_mais_caro = produto

        
        if preco < preco_min:
            preco_min = preco
            produto_mais_barato = produto


media_faturamento = faturamento_total / count

print("Faturamento total:", faturamento_total)
print("Produto mais caro:", produto_mais_caro, "-", preco_max)
print("Produto mais barato:", produto_mais_barato, "-", preco_min)
print("Média geral de faturamento:", media_faturamento)
