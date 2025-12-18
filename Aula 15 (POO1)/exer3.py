# Vamos criar uma classe ContaBancaria! O construtor (__init__) deve ter um saldo inicial. Crie um método depositar(valor) que aumenta o saldo. Crie um método mostrar_saldo() que mostra o saldo atual. Crie um objeto da classe e faça um depósito de R$ 100. Dica: use self.saldo para guardar o valor dentro do objeto.

class ContaBancaria:

    def __init__(self, saldo_Inicial):
        self.saldo_Inicial =  saldo_Inicial
    def depositar(self, valor):
        self.valor = valor 
        self.saldo_Inicial = self.saldo_Inicial + self.valor 
    def mostrar_saldo(self):
        print(f"Saldo atual:  {self.saldo_Inicial:}")

deposito =  ContaBancaria(500)
deposito.mostrar_saldo()
deposito.depositar(100)
deposito.mostrar_saldo()
        