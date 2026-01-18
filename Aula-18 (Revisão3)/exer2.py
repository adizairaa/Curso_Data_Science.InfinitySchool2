# Você tem uma lista de strings que deveriam ser números, mas alguns valores estão ausentes (''). Lista de Entrada: dados_brutos = ['10.5', '22', '', '4.5', '30'] Crie uma função chamada converter_para_numeros_float que receba esta lista e retorne uma nova lista contendo os valores convertidos para o tipo float. Se o valor for uma string vazia (''), ele deve ser substituído pelo número 0.0 (Imputação zero) na lista de saída.

def converter_para_numeros_float(lista_dados):
    dados_convertidos = []
    for valor in lista_dados:
        if valor == '':
            valor = 0.0
            dados_convertidos.append(valor)

        else:
            valor = float(valor)
            dados_convertidos.append(valor)
    return dados_convertidos        

dados_brutos = ['10.5', '22', '', '4.5', '30']

print(converter_para_numeros_float(dados_brutos))
        