# Crie um programa que solicite ao usuário a entrada de 5 números inteiros. 
# Utilize um contador para controlar quantas vezes o loop foi executado. 
# Utilize um acumulador para somar os números digitados. 
# Ao final, calcule e exiba a média dos números.

contador = 0
acumulador = 0 

while contador <5 :
    numero = int(input("Digite um numero inteiro: "))
    acumulador += numero 
    contador += 1
media = acumulador /5 
print("A media dos numeros digitado é:", media)