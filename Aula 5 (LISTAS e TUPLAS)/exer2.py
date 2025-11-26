# Crie um programa que gerencie uma lista de compras. O programa deve: Perguntar ao usuário quantos itens deseja adicionar.
# Utilizar um for para ler cada item e armazená-lo em uma lista. Após o cadastro, exibir a lista completa de compras. 
# Perguntar ao usuário se deseja remover algum item. 
# Se o usuário informar um item existente, remova-o da lista e exiba a lista atualizada.
lista_de_compras = []
quantidade = int(input("Você deseja adicionar quantos itens?: "))
for i in range(quantidade):
    item = input("Qual o item que você deseja adicionar: ")
    lista_de_compras.append(item)
print(f"lista de compras:", lista_de_compras)
remover = input("Você deseja remover algum item da lista?: ")
if remover == "sim":
    removido = input(f"Qual item deseja remover?:")
    for coisa in lista_de_compras:
        if coisa == removido:
            lista_de_compras.remove(coisa)
print(f"lista de compras:", lista_de_compras)