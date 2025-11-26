# Crie uma função chamada executar_pipeline que recebe uma lista de dados e uma função de transformação.
# A função deve aplicar a transformação em cada item da lista e retornar o resultado.
# Crie duas funções de transformação, uma que dobra um número e outra que adiciona 5.
# Use sua função executar_pipeline para aplicar primeiro a função que dobra na lista [1, 2, 3], depois aplique a função
# que adiciona 5 no resultado anterior.
# Imprima o resultado de cada aplicação.
def executar_pipeline(dados, funcao):
    return [funcao(item) for item in dados]
dados = [1, 2, 3]

def dobra (elemento):
    return elemento *2 
def adiciona(elemento):
    return elemento + 5

print (f'Resultado da dobra', executar_pipeline(dados,dobra))
print (f'Resultado da dobra',executar_pipeline (executar_pipeline(dados,dobra), adiciona))