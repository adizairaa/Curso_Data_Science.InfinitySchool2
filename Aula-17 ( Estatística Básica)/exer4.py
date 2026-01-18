# Você trabalha monitorando o tempo de uptime (tempo em que o servidor está funcionando) de dois servidores em uma semana (7 dias). Os dados de uptime (em horas) são: Servidor Alpha: [168, 167, 160, 168, 165, 150, 168] Servidor Beta: [160, 165, 168, 168, 165, 160, 165] Seu objetivo é gerar um mini-relatório estatístico comparativo usando Python para determinar: Qual servidor tem o melhor desempenho típico (maior Média)? Qual servidor é o mais confiável/consistente (menor Desvio Padrão)? Passos a serem programados: Importe a biblioteca statistics. Calcule a Média e o Desvio Padrão para o Servidor Alpha. Calcule a Média e o Desvio Padrão para o Servidor Beta. Crie um bloco de impressão que resuma os resultados e forneça uma conclusão clara sobre qual servidor você recomendaria, justificando com as métricas (Média e DP).
import statistics as est

servidor_alpha =[168, 167, 160, 168, 165, 150, 168]
servidor_beta = [160, 165, 168, 168, 165, 160, 165]

media_alpha = est.mean(servidor_alpha)
media_beta = est.mean(servidor_beta)

dv_alpha = est.stdev(servidor_alpha)
dv_beta = est.stdev(servidor_beta)

if media_alpha > media_beta:
    melhor_servidor =  "Servidor alpha"
else:
    melhor_servidor = "Servidor  beta"
print(f"O melhor servidor é {melhor_servidor}")

if dv_alpha > dv_beta:
    melhor_dv =  "dv_alpha"
else:
    melhor_dv = "dv_beta"
print(f"O melhor dv é {melhor_servidor}")