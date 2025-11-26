# Crie um arquivo chamado dados_desempenho.csv com o seguinte conteúdo (use vírgula , como delimitador):
#  Escreva um script Python que: Use o módulo csv para ler o arquivo dados_desempenho.csv, pulando o cabeçalho. 
# Para cada linha, calcule a Média das duas leituras (Leitura_1 e Leitura_2). 
# Imprima o ID do sensor e sua média calculada, garantindo que o valor seja um número.

import csv
dados = [
    ['ID_Sensor', 'Leitura_1', 'Leitura_2'],
    ['A01', '45.5', '55.2'],
    ['B02', '80.0', '75.0'],
    ['C03', '30.1', '20.5']
]

with open('dados_desempenho.csv', 'w', newline='') as d:
    writer = csv.writer (d , delimiter =",")
    writer.writerows(dados)
    
print("Arquivo'dados_desempenho.csv")

with open('dados_desempenho.csv', 'r', newline='') as d:
    leitor = csv.reader(d, delimiter=',')
    next(leitor)
    
    for linhas in leitor:
        ID_Sensor, Leitura_1, Leitura_2 = linhas
        media = (float(Leitura_1)+float(Leitura_2)) / 2 
        print(f'A média do {ID_Sensor} é {media}')