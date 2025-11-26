# Crie um programa que cadastre alguns produtos e suas quantidades. 
# Primeiro, pergunte quantos produtos o usuário deseja cadastrar. 
# Em seguida, use um laço for para repetir o pedido do nome e da quantidade do produto o número de vezes informado.
#  Durante o laço, mostre na tela cada produto cadastrado no formato: Produto: X | Quantidade: Y
quantidades_produtos = int(input("Quantos produtos você gostaria de cadastrar?:  "))
for i in range( quantidades_produtos):
    produto = str(input("Digite o nome do produto: "))
    quantidade = int(input(f"Digite a quantidade de {produto}: "))
    print(f"Produto: {produto} | Quantidade: {quantidade}")