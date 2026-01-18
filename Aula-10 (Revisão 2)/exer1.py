# Você tem a seguinte lista de produtos, cada um representado como uma tupla com (produto, preço unitário, quantidade):
# produtos = [ ("Maçã", 3.50, 4), ("Leite", 4.20, 2), ("Pão", 2.50, 6), ("Ovos", 0.80, 12) ] Tarefa:
# Crie um programa que percorra a lista de tuplas. Para cada produto, calcule o preço total (preço unitário × quantidade).
# Exiba na tela uma lista mostrando: 
# Nome do produto Quantidade Preço unitário Preço total do produto Dica: você pode usar um loop for para percorrer a lista de tuplas.

produtos = [ ("Maçã", 3.50, 4), ("Leite", 4.20, 2), ("Pão", 2.50, 6), ("Ovos", 0.80, 12) ]
 

for i in produtos:
    fruta, preco, quantidade = i
    preco_total= preco * quantidade
    print(f'{fruta}, preço unitario {preco}, preço total {preco_total}')