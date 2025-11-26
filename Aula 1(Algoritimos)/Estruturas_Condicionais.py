#Peça ao usuário duas notas para dois alunos (total de 4 notas). Calcule a média de cada aluno. 
# Exiba para cada aluno a mensagem correspondente: "Aprovado"
#  se a média for maior ou igual a 7; 
# "Recuperação" se a média for maior ou igual a 5 e menor que 7;
#  "Reprovado" se a média for menor que 5.

Aluno1 = str(input("Digite o nome do aluno 1 : "))
Aluno2 = str(input("Digite o nome do aluno 2 : "))
nota1_Aluno1 = int(input("Digite a primeira nota do aluno 1: "))
nota2_Aluno1 = int(input("Digite a segunda nota do aluno 1: "))
nota1_Aluno2 = int(input("Digite a primeira nota do aluno 2: "))
nota2_Aluno2 = int(input("Digite a segunda nota do aluno 2: "))
media1 = ( nota1_Aluno1 + nota2_Aluno1 )/2
print(f"A média do aluno {Aluno1} é {media1} ") 
if  media1 >=7:
    print(f"Aluno está APROVADO")
elif media1 >=5 and media1 <7:
    print(f"Aluno está em Recuperação") 
else: print(f"Aluno está Reprovado ")

media2 = ( nota1_Aluno2 + nota2_Aluno2 )/2
print(f"A média do aluno {Aluno2} é {media2} ") 
if  media2 >=7:
    print(f"Aluno está APROVADO")