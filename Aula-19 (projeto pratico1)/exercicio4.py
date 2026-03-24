
# # Agora vamos criar nossa primeira aplicação visual com o Streamlit! 
# # Crie um arquivo chamado app.py. 
# # Use as funções anteriores (buscar_cotacao, converter e registrar_historico). Crie campos para digitar as moedas e o valor. Mostre o resultado e o histórico direto na tela.
# # Dica: Para rodar, digite no terminal: streamlit run app.py

import streamlit as st

from funcoes import buscar_cotacao, converter, registrar_historico, historico

st.title("Monitor de Cotação")#TITULO 
st.write("Câmbio entre moedas e  o histórico.")#SUBTITULO 
moedas_disponiveis = [  'BRL','USD','EUR']

#Para O USO  DO SELETOR TIPO CAIXA 

moeda1 = st.selectbox("Moeda de Origem:", moedas_disponiveis, index = 0)
moeda2= st.selectbox("Moeda Câmbio:", moedas_disponiveis, index=1)

valor = st.number_input(
    "Digite o valor para converter:",
    min_value=0.0,
    format="%.2f")# lembrar de criar uma variavel global e de colocar o formato do 
#float para nao aparecer um numero enorme de numero

# Inicializa histórico na sessão

if "historico" not in st.session_state:
    st.session_state.historico = []

#  USODO BOTÃO 
if st.button("Buscar Taxa de Câmbio"):
    cotacao = buscar_cotacao(moeda1, moeda2)
    resultado = converter(valor, cotacao)

    registro_historico = f"{valor:} {moeda1} → {resultado} {moeda2}"
    st.session_state.historico.append(registro_historico)



    st.success(f"Resultado: {resultado} {moeda2}")
    st.write(f"Cotação atual: {cotacao}")

st.subheader("Histórico de Conversões")
if st.session_state.historico:
    for item in st.session_state.historico:
        st.write(item)
else:
    st.write("Nenhuma conversão realizada ainda.")