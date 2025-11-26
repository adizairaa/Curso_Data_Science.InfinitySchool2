#Conversor e Validador de Produtos:
#  Você recebeu um pequeno arquivo CSV com dados de produtos, mas ele contém inconsistências e 
# você precisa convertê-lo para JSON para importação em um novo sistema. 
# Arquivo de Entrada (Crie-o manualmente no seu ambiente de trabalho ou use o código):
#  ID,Nome,Preco_Unitario,Qtd_Estoque 101,Caneta Azul,2.50,100 102,Caderno A5,15.00 103,Lápis HB,1.00,50 104,Estojo,20.00 
# Inconsistência: Qtd vazia Tarefa: Criação: Crie o arquivo CSV de entrada (produtos_brutos.csv) com o cabeçalho e os
#  quatro registros acima. Importação e Validação: Leia o arquivo produtos_brutos.csv usando o módulo csv.
#  Tratamento de Inconsistência: Itere sobre as linhas. Se o campo Qtd_Estoque estiver vazio, ignore a linha (filtre-a).
#  Conversão: Para as linhas válidas, crie um dicionário Python com as chaves correspondentes ao cabeçalho. 
# Lembre-se de converter ID, Preco_Unitario e Qtd_Estoque para os tipos numéricos corretos (int ou float).
#  Exportação: Salve a lista final de dicionários limpos no arquivo JSON chamado produtos_limpos.json, 
# usando o módulo json e adicionando o parâmetro indent=4 para legibilidade.

import csv
import json

with open('produtos_brutos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Nome", "Preco_Unitario", "Qtd_Estoque"])
    writer.writerow([101, "Caneta Azul", "2.50", "100"])
    writer.writerow([102, "Caderno A5", "15.00", ""])
    writer.writerow([103, "Lápis HB", "1.00", "50"])
    writer.writerow([104, "Estojo", "20.00", ""])

produtos_limpos = []

with open('produtos_brutos.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for linha in reader:
        if linha["Qtd_Estoque"].strip() == "":
            continue
        produto = {
            "ID": int(linha["ID"]),
            "Nome": linha["Nome"],
            "Preco_Unitario": float(linha["Preco_Unitario"]),
            "Qtd_Estoque": int(linha["Qtd_Estoque"])
        }
        produtos_limpos.append(produto)

with open('produtos_limpos.json', 'w', encoding='utf-8') as json_file:
    json.dump(produtos_limpos, json_file, indent=4, ensure_ascii=False)
