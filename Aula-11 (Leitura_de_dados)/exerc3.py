# Defina um dicionário Python com dados de um usuário (por exemplo, nome, matricula e habilidades - 
# que deve ser uma lista). Use a função json.dump() para salvar este dicionário no arquivo cartao_usuario.json, formatado com indent=4. 
# Em seguida, escreva a lógica para carregar o conteúdo do arquivo cartao_usuario.json (usando json.load())
# de volta para uma nova variável Python. 
# Imprima o primeiro item da lista de habilidades lida do JSON e o tipo de dado da variável carregada.
import json 

dados_usuario = {
    "nome": "João Silva",
    "matricula": 202401,
    "habilidades": ["Python", "Linux", "Redes"]
}
with open ('cartao_usuario.json', 'w') as dados:
    json.dump( dados_usuario, dados, indent=4 )

with open ('cartao_usuario.json', 'r') as dados:
    dados_carregados = json.load(dados)
print(dados_carregados['habilidades'][2])