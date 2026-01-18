# Crie um código em Python que receba a lista codigos_brutos e realize as seguintes ações: Itere sobre a lista. Para cada código, remova todos os espaços em branco das extremidades (início e fim) usando o método apropriado. Converta o código resultante para letras maiúsculas para padronização. Armazene os códigos limpos em uma nova lista chamada codigos_limpos. Imprima a lista codigos_limpos ao final.
codigos_brutos = "  abc123  , xyz789 ,   teste456, CODIGO001   "

lista_codigo = codigos_brutos.split(",")

codigos_limpos = []


for codigo in lista_codigo:
    x = codigo.upper().strip()
    codigos_limpos.append(x)

print (f"{codigos_limpos}")

