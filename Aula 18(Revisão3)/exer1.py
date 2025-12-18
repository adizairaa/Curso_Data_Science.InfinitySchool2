# Você tem uma lista de cabeçalhos (chaves) e uma lista de dados que representa um único registro (valores). Lista de Chaves: chaves = ['ID', 'Nome', 'Status'] Lista de Valores: valores = ['15', 'Helena', 'Inativo'] Crie uma função chamada combinar_registro que receba estas duas listas e retorne um único dicionário onde cada chave do cabeçalho está mapeada para o seu respectivo valor.



def combinar_registro(valores, chaves):
    return dict (zip(chaves,valores  ))

chaves = ['ID', 'Nome', 'Status']
valores = ['15', 'Helena', 'Inativo']

print(combinar_registro(valores=valores, chaves= chaves))
