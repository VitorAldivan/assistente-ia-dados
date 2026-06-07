import streamlit as st

from src.data_loader import carregar_arquivo
from src.analysis import gerar_resumo
from src.analysis import gerar_contexto_llm
from src.llm import perguntar_dados


st.set_page_config(
    page_title="Assistente IA para Dados",
    layout="wide"
)

st.title("📊 Assistente IA para Dados")

arquivo = st.file_uploader(
    "Envie um arquivo CSV ou Excel",
    type=["csv", "xlsx"]
)

if arquivo:

    df = carregar_arquivo(arquivo)

    # mantém o dataframe inteiro disponível
    st.session_state["df"] = df

    st.success("Arquivo carregado com sucesso!")

    resumo = gerar_resumo(df)

    st.subheader("Indicadores Gerais")

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
            int(df.isnull().sum().sum())
        )

    st.subheader("Dados do Arquivo")

    st.write(
        f"Total de registros: {len(df)}"
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=700
    )

    st.subheader("🤖 Converse com seus Dados")

    st.info(
        "Você pode perguntar sobre linhas, colunas, valores específicos, estatísticas e padrões do dataset."
    )

    pergunta = st.text_area(
        "Digite sua pergunta",
        height=120,
        placeholder="""
Qual produto vendeu mais?
"""
    )

    if st.button("Perguntar"):

        if not pergunta.strip():

            st.warning(
                "Digite uma pergunta."
            )

        else:

            with st.spinner(
                "Analisando os dados..."
            ):

                contexto = gerar_contexto_llm(
                    st.session_state["df"]
                )

                resposta = perguntar_dados(
                    pergunta,
                    contexto
                )

            st.markdown("### Resposta")

            st.write(resposta)