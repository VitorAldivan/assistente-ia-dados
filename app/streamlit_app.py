import streamlit as st
import plotly.express as px

from src.data_loader import carregar_arquivo
from src.analysis import gerar_resumo
from src.analysis import gerar_contexto_llm
from src.llm import perguntar_dados
from src.utils import identificar_colunas_numericas


st.set_page_config(
    page_title="Assistente IA para Dados",
    layout="wide"
)

st.title("📊 Assistente IA para Dados")

arquivo = st.file_uploader(
    "Envie um CSV ou Excel",
    type=["csv", "xlsx"]
)

if arquivo:

    df = carregar_arquivo(arquivo)

    st.success("Arquivo carregado!")

    st.subheader("Prévia")

    st.dataframe(df.head())

    resumo = gerar_resumo(df)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Linhas", resumo["linhas"])

    with col2:
        st.metric("Colunas", resumo["colunas"])

    colunas_numericas = identificar_colunas_numericas(df)

    if colunas_numericas:

        st.subheader("Visualização")

        coluna = st.selectbox(
            "Selecione uma coluna numérica",
            colunas_numericas
        )

        fig = px.histogram(
            df,
            x=coluna
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Pergunte aos seus dados")

    pergunta = st.text_area(
        "Digite sua pergunta"
    )

    if st.button("Perguntar"):

        contexto = gerar_contexto_llm(df)

        resposta = perguntar_dados(
            pergunta,
            contexto
        )

        st.markdown("### Resposta")

        st.write(resposta)