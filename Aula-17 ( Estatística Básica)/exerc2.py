# Você recebeu uma lista de pontuações de testes de velocidade em milissegundos (tempos_resposta = [550, 480, 520, 550, 600]). Crie um programa que: Calcule a Variância Amostral desses tempos de resposta. Calcule o Desvio Padrão Amostral desses tempos de resposta. Calcule a Média dos tempos de resposta (como referência). Imprima todos os resultados, arredondando o Desvio Padrão e a Média para duas casas decimais, e explique brevemente no código por que o Desvio Padrão é mais fácil de interpretar do que a Variância.


import statistics as estatistica
tempos_resposta = [550, 480, 520, 550, 600]

var_amostral = estatistica.variance(tempos_resposta)
print(f"A variancia é: {var_amostral}")

desvio_padrao = estatistica.stdev(tempos_resposta)
print(f"O desvio padrão é : {desvio_padrao:.2f}")

media_tempos =  estatistica.mean(tempos_resposta)
print (f"A média é: {media_tempos:.2f}")

