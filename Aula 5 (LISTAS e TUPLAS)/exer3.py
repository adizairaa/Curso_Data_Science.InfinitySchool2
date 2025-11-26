# Crie um programa que armazene uma tupla de frutas disponíveis em uma feira.
# O programa deve: Criar uma tupla com pelo menos 5 frutas. Exibir todas as frutas disponíveis.
# Perguntar ao usuário o nome de uma fruta e informar se ela está disponível ou não na feira. 
# Exibir a quantidade total de frutas na tupla.

frutas = ("maçã", "banana", "laranja", "uva", "melancia")
print(" Frutas disponíveis na feira:")
for fruta in frutas:
    print(f" {fruta}")

fruta_escolhida = input("\nDigite o nome de uma fruta para verificar se está disponível: ").lower()#transforma todas as letras para minuscula
if fruta_escolhida in frutas:
    print(f"A fruta '{fruta_escolhida}' está disponível na feira!")
else:
    print(f" A fruta '{fruta_escolhida}' não está disponível na feira.")

print(f"\n Quantidade total de frutas na feira:{frutas}")