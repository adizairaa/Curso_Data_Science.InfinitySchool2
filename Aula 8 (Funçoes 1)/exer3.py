# Crie uma função desconto que recebe um preço e retorna o preço com 10% de desconto.
# A variável da taxa de desconto deve ser local à função.

def desconto (preco):
    taxa = 0.10 
    return preco - (preco * taxa )
print (desconto(5.0))