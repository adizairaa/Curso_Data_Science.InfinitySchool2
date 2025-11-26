# Você deve criar um programa simples em Python para simular um pipeline de vendas.
# O programa deve seguir os seguintes passos: Criar uma função para cadastrar os produtos disponíveis, 
# armazenando-os em um dicionário no formato: {"nome_produto": preco_unitario} Os produtos já estão definidos: 
# Camiseta – R$ 50,00 Tênis – R$ 200,00 Boné – R$ 40,00 Mochila – R$ 120,00 Jaqueta – R$ 300,00 
# Criar uma função que receba o nome do produto e a quantidade, retornando o valor total sem desconto. 
# Criar uma função que aplique um desconto de acordo com o tipo de pagamento: Pix → 10% de desconto Débito → 5% de desconto Crédito → sem desconto Criar uma função principal (processar_venda) que receba: Nome do produto Quantidade Tipo de pagamento E devolva o valor final da compra já com desconto aplicado. 
# Saída Esperada (exemplo) Produto: Camiseta | Quantidade: 2 | Pagamento: pix | Valor final: R$ 90.00 Crie 5 vendas.

def cadastrar_produtos():
    produtos = {
        "Camiseta": 50.00,
        "Tênis": 200.00,
        "Boné": 40.00,
        "Mochila": 120.00,
        "Jaqueta": 300.00
    }
    return produtos

def calcular_total(produto, quantidade, produtos):
    if produto not in produtos:
        return "Produto não encontrado!"
    return produtos[produto] * quantidade

def aplicar_desconto(valor, tipo_pagamento):
    tipo_pagamento = tipo_pagamento.lower()
    if tipo_pagamento == "pix":
        return valor * 0.90  # 10% de desconto
    elif tipo_pagamento == "débito" or tipo_pagamento == "debito":
        return valor * 0.95  # 5% de desconto
    elif tipo_pagamento == "crédito" or tipo_pagamento == "credito":
        return valor  # sem desconto
    else:
        return "Tipo de pagamento inválido!"

def processar_venda(produto, quantidade, tipo_pagamento, produtos):
    total_sem_desconto = calcular_total(produto, quantidade, produtos)
    
    
    if isinstance(total_sem_desconto, str):
        return total_sem_desconto
    
    valor_final = aplicar_desconto(total_sem_desconto, tipo_pagamento)
    
    if isinstance(valor_final, str):
        return valor_final
    
    return f"Produto: {produto} | Quantidade: {quantidade} | Pagamento: {tipo_pagamento} | Valor final: R$ {valor_final:.2f}"


produtos = cadastrar_produtos()

vendas = [
    processar_venda("Camiseta", 2, "pix", produtos),
    processar_venda("Tênis", 1, "crédito", produtos),
    processar_venda("Boné", 3, "débito", produtos),
    processar_venda("Mochila", 2, "pix", produtos),
    processar_venda("Jaqueta", 1, "débito", produtos),
]

for venda in vendas:
    print(venda)
