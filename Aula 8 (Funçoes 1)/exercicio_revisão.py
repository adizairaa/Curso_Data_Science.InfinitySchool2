# Crie um programa em Python que gerencie uma biblioteca digital simples utilizando listas, tuplas, dicionários e sets. 
# Passos que você deve seguir: Lista - Crie uma lista chamada livros com pelo menos 5 títulos de livros. 
# Tupla - Crie uma tupla chamada categorias com a categoria correspondente de cada livro da lista (mesma ordem). 
# Dicionário - Crie um dicionário chamado catalogo que organize os livros de acordo com suas categorias, de forma que cada categoria 
# seja uma chave e a lista de livros daquela categoria seja o valor.
# Set - Crie um conjunto (set) chamado usuarios com pelo menos 3 nomes de usuários cadastrados (sem repetições).
# Exiba na tela: Todos os livros disponíveis (lista) Todas as categorias (tupla) O catálogo (dicionário), mostrando a categoria e os livros associados A lista de usuários cadastrados (set) 
# Dica: você pode usar zip() e compreensão de listas para montar o catálogo automaticamente a partir da lista de livros e 
# da tupla de categorias. 
# Exemplo de saída esperada: Livros disponíveis: ['Dom Casmurro', 'O Senhor dos Anéis', '1984', 'O Pequeno Príncipe', 'A Revolução dos Bichos'] Categorias disponíveis: ('Romance', 'Fantasia', 'Ficção', 'Romance', 'Ficção') Catálogo da biblioteca: - Ficção: ['1984', 'A Revolução dos Bichos'] - Romance: ['Dom Casmurro', 'O Pequeno Príncipe'] - Fantasia: ['O Senhor dos Anéis']
# Usuários cadastrados: {'Carlos', 'Ana', 'Mariana'}

livros = ['Dom Casmurro', 'O Senhor dos Anéis', '1984', 'O Pequeno Príncipe', 'A Revolução dos Bichos']

categorias = ('Romance', 'Fantasia', 'Ficção', 'Romance', 'Ficção')


catalogo = {}
for livro, categoria in zip(livros, categorias):
    if categoria not in catalogo:
        catalogo[categoria] = []
    catalogo[categoria].append(livro)

usuarios = {'Carlos', 'Ana', 'Mariana'}

print(" Livros disponíveis:", livros)
print(" Categorias disponíveis:", categorias)
print("\nCatálogo da biblioteca:")
for categoria, lista_livros in catalogo.items():
    print(f"- {categoria}: {lista_livros}")
print(" Usuários cadastrados:", usuarios)
