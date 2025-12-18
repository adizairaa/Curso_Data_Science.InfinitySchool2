# Escreva um script Python que use o bloco with open() no modo de escrita ('w') para criar um arquivo chamado minhas_tarefas.txt.
#  Adicione as seguintes três linhas separadas ao arquivo: 1. Comprar material escolar 2. Enviar relatório técnico 3.
#  Estudar sobre JSON No mesmo script, use novamente o with open() no modo de leitura ('r') e um laço for para ler e imprimir cada linha do arquivo,
#  adicionando a tag [CONCLUIR] na frente de cada linha

arquivo = open('minhas_tarefas.txt.', 'w') 
arquivo.write('Comprar material escolar\n')
arquivo.write('Enviar relatório técnico\n')
arquivo.write('Estudar sobre JSON\n')
with open('minhas_tarefas.txt.', 'r') as arquivo:
    linhas = arquivo.readlines()
for linha in linhas:
    print(f"[CONCLUIR]{linha.strip()}")
