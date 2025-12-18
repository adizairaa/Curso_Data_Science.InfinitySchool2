# implemente um programa que cadastra alunos, guarda os dados em estruturas adequadas e gera relatórios simples.
# Use listas, tuplas, dicionários, sets e funções aprendidas em aula. 
# Etapas do Projeto Cadastro de alunos (Listas e Tuplas) Crie uma lista para armazenar os alunos. 
# Cada aluno será representado por uma tupla com (nome, idade, nota). Organização dos dados (Dicionários e Sets)
# Transforme a lista em um dicionário, onde a chave é o nome do aluno e o valor é outra tupla (idade, nota). 
# Use um set para armazenar as idades únicas dos alunos. Funções I – Operações básicas
# Crie uma função adicionar_aluno(nome, idade, nota) que adiciona um aluno ao dicionário. Crie uma função listar_alunos()que mostra todos os alunos. 
# Funções II – Relatórios Crie uma função media_notas() que retorna a média das notas. Crie uma função aluno_topo() que retorna o nome do aluno com maior nota. Crie uma função idades_unicas() que retorna o set com as idades sem repetição. 
# Exemplo de Saída esperada: Ana - Idade: 20, Nota: 8.5 Bruno - Idade: 22, Nota: 7.0 Carla - Idade: 20, Nota: 9.2 Média das notas: 8.2 Melhor aluno: Carla Idades únicas: {20, 22}

lista_alunos = []
dicionario_alunos = {}
idades_set = set()

def adicionar_aluno(nome, idade, nota):
    aluno = (nome, idade, nota)
    lista_alunos.append(aluno)
    dicionario_alunos[nome] = (idade, nota)
    idades_set.add(idade)

def listar_alunos():
    for nome, (idade, nota) in dicionario_alunos.items():
        print(f"{nome} - Idade: {idade}, Nota: {nota}")

def media_notas():
    if not dicionario_alunos:
        return 0
    return sum(nota for idade, nota in dicionario_alunos.values()) / len(dicionario_alunos)

def aluno_topo():
    if not dicionario_alunos:
        return None
    return max(dicionario_alunos.items(), key=lambda item: item[1][1])[0]

def idades_unicas():
    return idades_set

adicionar_aluno("Ana", 20, 8.5)
adicionar_aluno("Bruno", 22, 7.0)
adicionar_aluno("Carla", 20, 9.2)

listar_alunos()
print(f"Média das notas: {media_notas():.1f}")
print(f"Melhor aluno: {aluno_topo()}")
print(f"Idades únicas: {idades_unicas()}")
