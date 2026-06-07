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

    st.success("Arquivo carregado com sucesso!")

    st.subheader("Visualização dos Dados")

    st.write(f"Total de registros no dataset: {len(df)}")

    quantidade = st.slider(
        "Quantidade de linhas para visualizar",
        min_value=1,
        max_value=len(df),
        value=min(20, len(df))
    )

    st.dataframe(
        df.head(quantidade),
        use_container_width=True
    )

    resumo = gerar_resumo(df)

    st.subheader("Indicadores Gerais")

    total_nulos = int(
        df.isnull().sum().sum()
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Linhas",
            resumo["linhas"]
        )

    with col2:
        st.metric(
            "Colunas",
            resumo["colunas"]
        )

    with col3:
        st.metric(
            "Valores Nulos",
            total_nulos
        )

    colunas_numericas = identificar_colunas_numericas(df)

    if colunas_numericas:

        st.subheader("Visualizações")

        coluna = st.selectbox(
            "Selecione uma coluna numérica",
            colunas_numericas
        )

        st.markdown("### Histograma")

        fig_hist = px.histogram(
            df,
            x=coluna,
            title=f"Distribuição de {coluna}"
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

        st.markdown("### Boxplot")

        fig_box = px.box(
            df,
            y=coluna,
            title=f"Boxplot de {coluna}"
        )

        st.plotly_chart(
            fig_box,
            use_container_width=True
        )

    st.subheader("🤖 Pergunte aos seus Dados")

    pergunta = st.text_area(
        "Digite sua pergunta"
    )

    if st.button("Perguntar"):

        with st.spinner("Analisando os dados..."):

            contexto = gerar_contexto_llm(df)

            resposta = perguntar_dados(
                pergunta,
                contexto
            )

        st.markdown("### Resposta")

        st.write(resposta)