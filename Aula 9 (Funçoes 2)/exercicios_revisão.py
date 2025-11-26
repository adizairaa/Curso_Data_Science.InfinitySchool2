# O fatorial de um número inteiro positivo n (escrito como n!) é o produto de todos os números inteiros de 1 até n. 
# Exemplo: 5! = 5 × 4× 3 × 2 ×1 = 120 Crie uma função chamada fatorial(numero) que: Receba um número inteiro positivo. 
# Retorne o fatorial desse número. 
# No programa principal, peça ao usuário para digitar um número e exiba o resultado chamando a função.

def fatorial(numero):
    if numero < 0:
        return "Número inválido! Digite um inteiro positivo."

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

n = int(input("Digite um número inteiro positivo: "))
print(f"O fatorial de {n} é {fatorial(n)}")
