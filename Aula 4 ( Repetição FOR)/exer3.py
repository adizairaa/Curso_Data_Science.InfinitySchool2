# Crie um programa que peça ao usuário uma palavra e, usando um loop for, conte quantas vogais existem nessa palavra. 
# Ao final, exiba a quantidade total de vogais encontradas.
total_vogais = ""
vogais = "aeiouAEIOU"

palavra = str(input("Digite uma palavra: ")) 
for letra in palavra :
    if letra.isalpha ():
        if letra in  vogais :
            total_vogais += letra
print(f"O total de vogais é: {total_vogais}")