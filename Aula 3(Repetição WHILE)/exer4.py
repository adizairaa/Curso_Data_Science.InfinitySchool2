# Você deve criar um programa que continue pedindo uma senha ao usuário até que a senha correta seja digitada.
# O programa deve informar quando a senha estiver incorreta e liberar o acesso somente ao acerto. 
# Passo a passo: Definir a senha correta Essa senha pode estar armazenada em uma variável, como por exemplo "1234". 
# Criar uma variável para armazenar a senha digitada Inicialmente, essa variável pode estar vazia ("") para entrar no loop.
# Usar um loop while para repetir a solicitação A condição do while será que a senha digitada seja diferente da senha correta. Dentro do loop, pedir a senha ao usuário com input() Comparar o valor digitado com a senha correta. Se a senha estiver correta, exibir mensagem de acesso liberado e encerrar o programa.
# Se a senha estiver errada, avisar e continuar solicitando.

senha_correta = "1234"
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("Digite sua senha")
    if senha_digitada == senha_correta:
        print("Acesso liberado")
        break
    else:
        print("Senha incorreta, tente novamente")