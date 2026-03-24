import streamlit as st
import pandas as pd


dados = {
    "Nome": ["Adila", "Alex","Aurea", "Paulo", "Amanda", "Carla", "Bruno"],
    "Função": ["Analista", "Desenvolvedor", "Analista", "Gerente", "Desenvolvedor", "Analista", "Gerente"]
}

df = pd.DataFrame(dados)

# chamada de título
st.title("Simulação de Consulta de Dados")

# para exibir tabelas
st.subheader("Tabela de Funcionários")
st.dataframe(df)


contagem_funcoes = df["Função"].value_counts()

# Exibir gráficos
st.subheader("Quantidade de pessoas por função")
st.bar_chart(contagem_funcoes)  