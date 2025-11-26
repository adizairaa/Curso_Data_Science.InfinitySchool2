# Projeto Final - Sistema de Cadastro de Alunos Objetivo Desenvolva um programa que cadastre 3 alunos, colete suas notas e apresente um relatório final com a situação de cada um. 
# Funcionalidades esperadas: 
# 1. Cadastro de dados Solicite o nome de 3 alunos Para cada aluno, peça sua nota (0 a 10) 
# Armazene os dados em listas separadas 2. Processamento Para cada nota, determine a situação: 
# Nota ≥ 7: "Aprovado" Nota ≥ 5 e < 7: "Recuperação" Nota < 5: "Reprovado" 3. 
# Relatório final Exiba uma tabela organizada com: Nome do aluno Nota obtida Situação acadêmica Exemplo de saída esperada:
# Nome Nota Situação ----------------------------- Maria 9.0 Aprovado Renato 6.0 Recuperação Alan 3.0 Reprovado onceitos que você deve aplicar: 
# Listas para armazenar nomes e notas Loop for com range() para coletar dados Estruturas condicionais para classificar situações 
# Formatação de saída com espaçamento adequado

lista_alunos = []
lista_nota = []
lista_tabela = []

for i in range (3):
    aluno = (input("Digite o nome do aluno : "))
    nota = int(input("Digite a primeira nota de 1 a 10: "))
    lista_alunos.append(aluno)
    lista_nota.append(nota)
    if nota >= 7:
        lista_tabela.append(f"nome:{lista_alunos[i]}, nota: {lista_nota[i]}, Aprovado ")
    elif nota >= 5 and nota < 7:
        lista_tabela.append(f"nome: {lista_alunos[i]}, nota: {lista_nota[i]}, Recuperação")
    else :
        lista_tabela.append (f"nome: {lista_alunos[i]}, nota: {lista_nota[i]}, Reprovado")
for linha in lista_tabela:
    print(f" {linha}")