# Vamos começar descobrindo quanto vale uma moeda em relação a outra! Crie um arquivo chamado etapa1.py. Importe o módulo requests. Crie uma função chamada buscar_cotacao(moeda_base, moeda_destino). Ela deve acessar a AwesomeAPI (https://economia.awesomeapi.com.br/json/last/ ) e devolver o valor atual da cotação. Exiba o valor no terminal com print(). Dica: o formato da URL é assim: https://economia.awesomeapi.com.br/json/last/USD-BRL
import requests 
import json

def buscar_cotacao(moeda_base, moeda_destino):
    url=f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    cotacao = requests.get(url)
    cotacao_json= cotacao.json()
    valor_bid = cotacao_json[f'{moeda_base}{moeda_destino}']['bid']
    return valor_bid    
cotacao_dolar = buscar_cotacao('EUR','USD')
print (f"cotação dolar hoje {cotacao_dolar}")