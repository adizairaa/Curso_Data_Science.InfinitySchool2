# Compare a consistência de dois grupos de investidores, analisando seus lucros diários (em R$ mil). Grupo X: [10, 12, 8, 10, 15] Grupo Y: [11, 10, 10, 10, 14] Crie um programa que: Calcule e imprima a Média e o Desvio Padrão (DP) para o Grupo X. Calcule e imprima a Média e o Desvio Padrão (DP) para o Grupo Y. Ao final, use um print() para determinar qual grupo é o mais consistente em seus lucros diários (o mais consistente é o que tem o menor DP) e justifique brevemente.
import statistics as estatistica

Grupo_X =  [10, 12, 8, 10, 15]
Grupo_Y =  [11, 10, 10, 10, 14]

media_grupoX = estatistica.mean(Grupo_X)
print (f"A media do grupo X é : {media_grupoX}")
dv_grupoX = estatistica.stdev(Grupo_X)
print (f"O desvio padrão do grupo X é : {dv_grupoX:.2f}")

media_grupoY = estatistica.mean(Grupo_Y)
print (f"A media do grupo Y é : {media_grupoY}")
dv_grupoY = estatistica.stdev(Grupo_Y)
print (f"O desvio padrão do grupo Y é : {dv_grupoY:.2f}")