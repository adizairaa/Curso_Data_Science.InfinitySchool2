# Você recebeu um pequeno texto e precisa analisar a frequência das palavras e identificar quais são únicas. 
# texto = "maçã banana laranja maçã pera banana laranja laranja" Tarefas: 
# Crie uma função chamada contar_palavras que receba o texto como string e retorne um dicionário onde: 
# a chave é a palavra o valor é a quantidade de vezes que a palavra aparece no texto 
# Crie uma função chamada palavras_unicas que receba o dicionário e retorne um set contendo apenas as palavras que aparecem uma única vez no texto. Imprima o dicionário de contagem e o set de palavras únicas. 
# Dica: Para criar o set de palavras únicas, percorra o dicionário e selecione apenas as palavras cujo valor seja 1.

def contar_palavra(texto):
    palavra = ''
    lista = []
    contagem ={}
    for i in texto:# cada palavra do texto em 1 elemento da lista
        palavra += i 
        if i == ' ': 
            lista.append(palavra)
            palavra = ""
    print(lista)
    for i in lista:# avalia cada elemento da lista caso ele ainda não exista coloca 1 (else) eo if avalia se ele aparece novamente
        if i in contagem:
            contagem[i]+=1 
        else:
            contagem[i]=1
    print(contagem)
    return contagem

def palavras_unicas(dic):
    unicas = set()
    for chave, valor in dic.items():
        if valor == 1:
            unicas.add(chave)
    return unicas

texto = 'maçã banana laranja maçã pera banana laranja laranja'
contar_palavra(texto)   
print(palavras_unicas(contar_palavra(texto)))