
print("🛒 Sistema de Registro de Vendas")
print("Digite 0 para finalizar a compra.\n")
total = 0.0  # Acumulador do valor total da compra
while True:
    preco = float(input("Digite o preço do item (ou 0 para finalizar): R$ "))

    if preco == 0:
        break  
    
    total += preco  
    print(f"Subtotal até agora: R$ {total:.2f}\n")

print(f"💰 Total da compra: R$ {total:.2f}")
