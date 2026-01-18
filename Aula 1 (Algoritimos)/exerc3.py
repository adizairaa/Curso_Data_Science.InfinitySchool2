# Crie um programa em Python que: Crie uma constante chamada PI com o valor 3.14159. 
# Crie uma variável chamada raio e atribua o valor 5. 
# Calcule a área do círculo (fórmula: PI * raio * raio) e guarde em uma variável chamada area.
#  Imprima na tela o resultado. Crie um outro programa em Python que: Pergunte ao usuário seu nome e sua idade. 
# Imprima a mensagem: Olá, <nome>! Você tem <idade> anos.

PI = 3.14159
raio = 5
area_raio = PI * raio * raio
print(area_raio)

nome = str(input("Digite seu nome: "))
idade = int(input("Digite a sua idade: "))
print(f"Olá, {nome}! Você tem {idade} anos")