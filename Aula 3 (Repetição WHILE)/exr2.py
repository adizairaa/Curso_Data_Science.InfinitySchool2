# Crie um programa que peça ao usuário para digitar a senha até que ele acerte.
# A senha correta é "senha123". Utilize a estrutura while para repetir a solicitação da senha. 
# Quando o usuário digitar a senha correta, exiba a mensagem "Acesso concedido!". 
# Garanta que o programa continue pedindo a senha enquanto o valor digitado estiver incorreto.

senha = ""
while senha != "123":
    senha = input ("digite a senha")
print("Acessso Liberado")