# Mostrar uma mensagem de boas-vindas com o nome e cidade. 
# Mostrar a idade do usuário. 
# Mostrar o valor do IMC com 2 casas decimais. 
# Tratar entradas para garantir que peso e altura sejam números válidos.

nome = str(input("Digite seu nome: "))
idade = int(input("Digite a sua idade: "))
cidade = str(input("Digite o nome da cidade onde você mora: "))
print(f"Olá{nome}, de {cidade}! Seja bem-vindo(o)!")
print(f"Sua idade é {idade}anos!")
peso = int(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))
IMC = peso / (altura * altura)

if IMC < 18.5:
    print("Você está abaixo do seu peso ideal!")
if IMC >= 18.5 and IMC <= 24.9:# Em python quando você faz comparações compostas , vc presisa repetir a variavelda condição
     print("Você está no seu peso ideal!")
if  IMC >25:
    print("Você está com sobrepeso!")   
if IMC >=25 and IMC <= 29.9:
    print("Você está Pré-obeso!") 
if IMC >=30 and IMC <=34.9:
    print("Você está é considerado Obeso I!")              
if IMC >=35 and IMC<=39.9:
    print("Você está é considerado Obeso Ii!")
if IMC > 40:
    print("Você está é considerado Obeso III!")            


print(f"Seu IMC é de: {IMC}")