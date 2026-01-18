precos_brutos = ["R$ 50,00", "R$120,50", " R$  9,90 ", "R$300,00"]

precos_numericos = []

for preco in precos_brutos:
  
    preco_limpo = preco.replace("R$", "")

    preco_limpo = preco_limpo.replace(",", ".")

    preco_limpo = preco_limpo.strip()
  
    preco_float = float(preco_limpo)
    
    precos_numericos.append(preco_float)

print(precos_numericos)
print(type(precos_numericos[0]))
