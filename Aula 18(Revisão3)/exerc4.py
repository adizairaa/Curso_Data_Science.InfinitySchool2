# Utilizando o conjunto de dados com o novo campo Faixa_Etaria (Jovem/Adulto), execute as seguintes análises e exporte o resultado: Agrupamento: Calcule a Média Salarial separadamente para cada Faixa_Etaria. Agrupamento: Calcule a Contagem de registros (Total de Pessoas) separadamente para cada Faixa_Etaria. Exportação: Crie um novo arquivo CSV chamado performance_faixa_etaria.csv. Este arquivo deve ter apenas 3 colunas: Faixa_Etaria, Media_Salarial e Total_Pessoas. Cada linha deve representar uma faixa etária.

import csv

arquivo_entrada = 'Faixa_Etaria.csv'
arquivo_saida = 'performance_faixa_etaria.csv'


dados_faixa = {}


with open(arquivo_entrada, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        faixa = linha['Faixa_Etaria']
        salario = float(linha['Salario'])

        if faixa not in dados_faixa:
            dados_faixa[faixa] = {
                'soma_salarios': 0,
                'total_pessoas': 0
            }

        dados_faixa[faixa]['soma_salarios'] += salario
        dados_faixa[faixa]['total_pessoas'] += 1


with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Faixa_Etaria', 'Media_Salarial', 'Total_Pessoas'])

    for faixa, valores in dados_faixa.items():
        media_salarial = valores['soma_salarios'] / valores['total_pessoas']
        escritor.writerow([
            faixa,
            round(media_salarial, 2),
            valores['total_pessoas']
        ])

print("Arquivo 'performance_faixa_etaria.csv' criado com sucesso!")

