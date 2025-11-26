# Escreva uma função que simule um caixa eletrônico. 
# A função saque deve receber o saldo atual da conta e o valor do saque. 
# Ela deve verificar se o saldo é suficiente para o saque. 
# Se for, deve imprimir 'Saque de R$ [valor] realizado com sucesso!' e o novo saldo. 
# Se não for, deve imprimir 'Saldo insuficiente.' e o saldo atual. 
# Chame a função para dois cenários: um com saque válido e outro com saque inválido.

def novo_saldo(saldo_atual, saque):
   if saldo_atual < saque:
      print(f'Saldo insuficiente')
   else:
      print(f'Saque de R${saque} realizado com sucesso')
      saldo_novo = saldo_atual - saque 
      print(f'O seu novo valor de saldo é de {saldo_novo}')

saque1 =   novo_saldo(250,1200)
saque2 =   novo_saldo(2500,1120)