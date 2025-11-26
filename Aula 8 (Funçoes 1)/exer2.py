# # Crie uma função cadastro que receba nome, idade e cidade usando **kwargs, e exiba cada dado.
# Crie uma função cadastro que receba nome, idade e cidade usando **kwargs, e exiba cada dado.

def cadastro(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
cadastro (nome= 'Adila', idade= 29, cidade = "São Paulo", cor= 'azul')
