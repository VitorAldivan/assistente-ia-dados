import pandas as pd


def gerar_resumo(df):
    return {
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "nomes_colunas": list(df.columns),
        "nulos": df.isnull().sum().to_dict(),
    }


def gerar_contexto_llm(df):
    """
    Cria um contexto muito mais rico para o Gemini.
    """

    contexto = []

    contexto.append(
        f"Dataset com {df.shape[0]} linhas e {df.shape[1]} colunas."
    )

    contexto.append(
        f"Colunas disponíveis: {list(df.columns)}"
    )

    contexto.append(
        "\nPrimeiras linhas:"
    )

    contexto.append(
        df.head(20).to_string()
    )

    contexto.append(
        "\nTipos das colunas:"
    )

    contexto.append(
        df.dtypes.to_string()
    )

    numericas = df.select_dtypes(
        include="number"
    )

    if not numericas.empty:

        contexto.append(
            "\nResumo estatístico:"
        )

        contexto.append(
            numericas.describe().to_string()
        )

    categoricas = df.select_dtypes(
        exclude="number"
    )

    if not categoricas.empty:

        contexto.append(
            "\nValores únicos:"
        )

        for coluna in categoricas.columns:

            valores = (
                categoricas[coluna]
                .dropna()
                .unique()
                .tolist()
            )

            contexto.append(
                f"{coluna}: {valores[:20]}"
            )

    return "\n".join(contexto)