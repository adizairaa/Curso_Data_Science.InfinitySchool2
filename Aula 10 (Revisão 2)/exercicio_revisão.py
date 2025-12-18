# Crie uma função que receba uma lista de preços de produtos e retorne uma nova lista com os preços já com 10% de desconto.
# Faça primeiro usando uma função normal e depois usando uma função lambda com map.
# Exemplo de lista de preços: [50.0, 120.0, 35.5, 80.0, 15.0].

def aplicar_desconto(lista):
    nova_lista = []
    for preco in lista:
        nova_lista.append(preco * 0.9)
    return nova_lista

print(aplicar_desconto(precos))

desconto_lambda = list(map(lambda x: x * 0.9, precos))
print(desconto_lambda)
