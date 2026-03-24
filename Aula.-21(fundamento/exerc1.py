
inventario = [
    {"nome":'Produto 1', "preco":1000, "estoque":10},
    {"nome":'Produto 2', "preco":500, "estoque":20},
    {"nome":'Produto 3', "preco":11, "estoque":3 },

]
def aumentar_preco(dicionario , porcentagem):
    novo_preco = dicionario["preco"] * (1 + porcentagem)
    return novo_preco



for posicao in range(len(inventario)):
        novo_preco = aumentar_preco(inventario[posicao], 0.05)
        print(f'Produto:{inventario[posicao]['nome']}\nPreço atualizado: R${novo_preco}')