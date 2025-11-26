# Crie uma calculadora que execute as quatro operações matemáticas básicas (soma, subtração, multiplicação e divisão) 
# com dois números inteiros fornecidos pelo usuário. O que seu programa deve fazer: 
# Perguntar ao usuário qual operação ele deseja realizar Solicitar dois números inteiros Executar a operação escolhida 
# Exibir o resultado Requisitos obrigatórios: Funções (4 funções obrigatórias): soma(numero1, numero2) - 
# retorna a soma subtracao(numero1, numero2) - retorna a subtração multiplicacao(numero1, numero2) - 
# retorna a multiplicação divisao(numero1, numero2) - retorna a divisão Entrada de dados: 
# Capturar a operação desejada usando input() Capturar dois números inteiros usando input() e int() Lógica de controle:
#  Usar if/elif/else para identificar qual operação executar
# Usar .lower() para comparar a operação (ignorar maiúsculas/minúsculas) Chamar a função correspondente Saída:
#  Exibir o resultado formatado mostrando a operação e o valor calculado Exemplo de execução: 
# Digite o tipo de operação que deseja fazer: soma, subtração, multiplicação, divisão soma Digite o primeiro número: 
# 10 Digite o segundo número: 5 O resultado da soma foi 15

def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    if numero2 == 0:
        return "Erro! Não é possível dividir por zero."
    return numero1 / numero2

operacao = input("Digite a operação desejada (soma, subtração, multiplicação, divisão): ").lower()

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

if operacao == "soma":
    resultado = soma(numero1, numero2)
    print(f"O resultado da soma entre {numero1} e {numero2} é: {resultado}")

elif operacao == "subtração" or operacao == "subtracao":
    resultado = subtracao(numero1, numero2)
    print(f"O resultado da subtração entre {numero1} e {numero2} é: {resultado}")

elif operacao == "multiplicação" or operacao == "multiplicacao":
    resultado = multiplicacao(numero1, numero2)
    print(f"O resultado da multiplicação entre {numero1} e {numero2} é: {resultado}")

elif operacao == "divisão" or operacao == "divisao":
    resultado = divisao(numero1, numero2)
    print(f"O resultado da divisão entre {numero1} e {numero2} é: {resultado}")

else:
    print("Operação inválida! Por favor, escolha entre: soma, subtração, multiplicação ou divisão.")
