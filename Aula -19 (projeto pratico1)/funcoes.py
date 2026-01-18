 # Vamos guardar as conversões feitas! Crie uma função registrar_historico(moeda, valor, resultado). Ela deve adicionar essas informações a uma lista chamada historico. Ao final, mostre todas as conversões já feitas.

import requests 
import json

# Lista global para guardar histórico
historico = []

def buscar_cotacao(moeda_base, moeda_destino):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda_base}-{moeda_destino}"
    response = requests.get(url)
    dados = response.json()
    return float(dados[f"{moeda_base}{moeda_destino}"]["bid"])

def converter(valor, cotacao):
    return valor * cotacao

def registrar_historico(moeda_origem, moeda_destino, valor, resultado):
    registro = f"{valor:.2f} {moeda_origem}  {resultado:.2f} {moeda_destino}"
    historico.append(registro)
    historico = []