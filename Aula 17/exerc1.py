# Defina uma lista chamada alturas_atletas com os seguintes valores (em metros): [1.85, 1.93, 1.78, 1.90, 1.85, 2.05, 1.75]. Importe a biblioteca necessária para os cálculos estatísticos. Calcule a Média das alturas. Calcule a Mediana das alturas. Calcule a Moda das alturas. Imprima todos os resultados de forma clara, com duas casas decimais, acompanhados de uma breve descrição (Ex: "Média das Alturas: X.XX m").

import statistics as estatistica

alturas_atletas = [1.85, 1.93, 1.78, 1.90, 1.85, 2.05, 1.75]
media_altura =  estatistica.mean(alturas_atletas)
print(f"Média das Alturas: {media_altura:.2f}m.")

mediana_altura =  estatistica.median(alturas_atletas)
print(f"Médiana das Alturas: {mediana_altura:.2f}m.")

moda_altura = estatistica.mode(alturas_atletas)
print(f"Moda das Alturas: {moda_altura:.2f}m.")