#Crie um programa que peça ao usuário um número inteiro e determine: 
# Se o número é positivo, negativo ou zero. 
# Se o número é par ou ímpar (apenas se for diferente de zero). O programa deve exibir mensagens como: 
# "Número positivo e par" "Número negativo e ímpar" "Número é zero"

numero = int (input(f"Digite um numero inteiro:"))
if numero == 0:
    print ("numero é igual a zero")
elif numero > 0  and numero %2 == 0:
   print("o numero é par e positivo")
elif numero > 0 and numero  %2 != 0:
   print ("o numero é impar e positivo")
elif numero < 0 and numero  %2 == 0:
   print ("o numero é par e negativo") 
else:
   print ("o numero é impar e negativo") 

i = 0 
while i < 5:
    print("Olá")
    i+=1