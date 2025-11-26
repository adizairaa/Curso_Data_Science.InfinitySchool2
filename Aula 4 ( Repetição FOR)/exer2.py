# Crie um programa que peça ao usuário para digitar uma palavra. 
# Em seguida, utilize um laço for para percorrer cada letra da string e exibi-la uma por linha.
palavra = str(input("Digite uma palavra: ")) 
for letra in palavra:
    print(f"letra atual:{letra}")