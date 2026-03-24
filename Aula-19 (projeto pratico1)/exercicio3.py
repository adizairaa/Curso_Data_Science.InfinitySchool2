# Vamos guardar as conversões feitas! Crie uma função registrar_historico(moeda, valor, resultado). Ela deve adicionar essas informações a uma lista chamada historico. Ao final, mostre todas as conversões já feitas.

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


import requests 


def buscar_cotacao(moeda_base, moeda_destino):
    url=f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    cotacao = requests.get(url)
    cotacao_json= cotacao.json()
    valor_bid = cotacao_json[f'{moeda_base}{moeda_destino}']['bid']
    valor_bid1=float(valor_bid)
    return valor_bid1    

def converter(valor, cotacao):
    return valor * cotacao

moeda_base = "BRL"
moeda_cambio = "USD"   

cotacao_dolar = buscar_cotacao(moeda_base, moeda_cambio)
print(cotacao_dolar)
valor = float(input("Digite o valor em real  que quer converter: "))
conversao_real = converter(valor,cotacao_dolar)
print(f"O valor é {conversao_real}")

# cotacao_dolar = buscar_cotacao('EUR','USD')
# print (f"cotação dolar hoje {cotacao_dolar}")