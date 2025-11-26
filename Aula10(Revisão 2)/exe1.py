# Crie uma função que receba uma lista de preços de produtos e retorne uma nova lista com os preços já com 10% de desconto. 
# Faça primeiro usando uma função normal e depois usando uma função lambda com map. 
# Exemplo de lista de preços: [50.0, 120.0, 35.5, 80.0, 15.0].

precos = [50.0, 120.0, 35.5, 80.0, 15.0]

def aplicar_desconto(lista):
    novo_preco = []
    for preco in lista:
        novo_preco.append(preco * 0.9)
    return novo_preco

print(aplicar_desconto(precos))