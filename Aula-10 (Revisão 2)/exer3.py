# Crie uma função que recebe uma lista de números e retorna uma nova lista apenas com os números pares, usando uma função normal e 
# depois usando uma função lambda com filter. 
# Exemplo de lista de números: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

def filtrar_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

print[filtrar_pares(numeros)]


pares_lambda = list[filter(lambda x: x % 2 == 0, numeros)]
print(pares_lambda)