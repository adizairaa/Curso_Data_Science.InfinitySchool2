# Dada a lista temperaturas = [30, 32, 31, 28, 29], calcule a média usando for.
temperaturas = [30, 32, 31, 28, 29]
soma = 0
for temp in temperaturas:
    soma += temp
media = soma / len(temperaturas)

print(f"A média das temperaturas é: {media:.1f}°C")
