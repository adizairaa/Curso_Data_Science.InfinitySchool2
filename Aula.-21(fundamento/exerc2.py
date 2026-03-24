def classificar_cliente(valor_gasto_total):
    if valor_gasto_total >= 1000:
        return "Ouro (Análise Preditiva)"
    elif valor_gasto_total >= 500 and valor_gasto_total <1000:
        return "Prata (Análise Descritiva)"
    return "Bronze (Requer Atenção)"

cliente1 =1200 
cliente2 =450

gastos_cliente = classificar_cliente(cliente1)
print(f'{gastos_cliente}')