dados = [20, 22, 25, 23, 24, 200]

import statistics

dados = [20, 22, 25, 23, 24, 200]

media = statistics.mean(dados)
mediana = statistics.median(dados)
moda = statistics.mode(dados)
desvio_padrao = statistics.stdev(dados)

print("📊 Relatório Estatístico Descritivo")
print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")
print(f"Desvio Padrão Amostral: {desvio_padrao:.2f}")

print("\n📝 Interpretação:")
print(
    "A diferença entre a média e a mediana indica uma distribuição assimétrica à direita, "
    "provocada pelo valor extremo 200. "
    "O desvio padrão elevado mostra que os dados apresentam baixa consistência e alta dispersão."
)
 