# Você deve criar um programa em Python que simule a organização de uma pequena pesquisa de opinião. 
# O objetivo é revisar os conceitos de listas, tuplas, dicionários e sets em um único exercício.
# Você recebeu os seguintes dados já organizados: #
#  Lista – Participantes cadastrados participantes = ["Ana", "Carlos", "Maria", "João", "Ana", "Mario", "Alice", "Alice"] # Tupla – Opções de lazer escolhidas na mesma ordem dos participantes opcoes_lazer = ("Cinema", "Esportes", "Leitura", "Música") Com base nesses dados, faça o seguinte: Crie um set chamado participantes_unicos a partir da lista para remover duplicatas. Crie um dicionário chamado lazer_favorito que relacione cada participante com sua opção de lazer correspondente, usando enumerate para percorrer a lista e a tupla juntos. Dica: use o operador módulo para evitar erros caso as listas tenham tamanhos diferentes: opcoes_lazer[i % len(opcoes_lazer)] Exiba os dados: A lista original de participantes. O set de participantes únicos. A tupla com as opções de lazer. O dicionário mostrando cada participante e sua atividade favorita. Peça ao usuário o nome de um participante e exiba sua atividade favorita (ou “não encontrado” se não existir). 
# Crie um resumo que mostre quantas pessoas escolheram cada atividade favorita.

participantes = ["Ana", "Carlos", "Maria", "João", "Ana", "Mario", "Alice", "Alice"]
opcoes_lazer = ("Cinema", "Esportes", "Leitura", "Música")

participantes_unicos = set(participantes)
lazer_favorito = {participantes[i]: opcoes_lazer[i % len(opcoes_lazer)] for i in range(len(participantes))}

print("Participantes:", participantes)
print("Participantes únicos:", participantes_unicos)
print("Opções de lazer:", opcoes_lazer)
print("Lazer favorito por participante:", lazer_favorito)

nome = input("Digite o nome de um participante: ")
print("Atividade favorita:", lazer_favorito.get(nome, "não encontrado"))

resumo = {}
for atividade in lazer_favorito.values():
    resumo[atividade] = resumo.get(atividade, 0) + 1

print("Resumo das atividades favoritas:", resumo)
