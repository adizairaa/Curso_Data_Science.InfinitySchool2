# Você foi contratado para criar um programa simples de cadastro de funcionários para uma pequena empresa.
# O programa deve: Solicitar as seguintes informações do funcionário: 
# Nome completo (texto) Idade (número inteiro) Salário mensal (número decimal) Processar as informações:
# Verificar se o funcionário é maior de idade (18 anos ou mais) Calcular o salário anual (salário mensal × 12)
# Exibir um relatório final contendo: Dados pessoais do funcionário Se ele é maior de idade 
# Salário anual Instruções técnicas: 
# Use a função input() para capturar os dados Use int() para converter a idade Use float() para converter o salário 
# Use estruturas condicionais (if, elif, else) para as verificações

nome = str(input("Digite seu nome: "))
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o valor do seu salario: "))
if idade >= 18:
    salario_anual = salario * 12
    print(f"Seu salario anual é: {salario_anual}")
else:
    print ("Você ainda é menor de idade")