# Crie um dicionário vendas que armazena o número de vendas por vendedor. 
# As chaves são os nomes e os valores são as vendas (ex: {"Ana": 10, "Bruno": 15, "Carla": 8}). 
# Adicione um novo vendedor, "Pedro", com 12 vendas. 
# Depois, remova a vendedora "Carla" do dicionário. Por fim, calcule e imprima a soma total de todas as vendas restantes.

vendas = {"Ana": 10, "Bruno": 15, "Carla": 8}
print(vendas)
vendas["Pedro"] = 12
print(vendas)
del vendas["Carla"]
print(vendas)

total_vendas = sum(vendas.values())
print(f"O total de vendas é: R$", total_vendas)