# Agora, vamos deixar nossa classe mais inteligente! Adicione o método especial __init__ à classe Pessoa. Esse método deve receber o nome da pessoa e guardar em um atributo self.nome. No método saudar(), mostre o nome da pessoa junto com a mensagem. Dica: o __init__ é chamado automaticamente quando criamos o objeto!
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def saudar(self):
        print (f"Bem- vindo {self.nome} ")

aluno1 = Pessoa("Adila")# lembrar de definir o objeto como a classe 
aluno1.saudar() # chamar o metodo qué e o comportamento esperado 