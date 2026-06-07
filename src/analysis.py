def gerar_resumo(df):
    """
    Gera resumo dos dados para exibição e IA.
    """

    resumo = {
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "nomes_colunas": list(df.columns),
        "nulos": df.isnull().sum().to_dict(),
    }

    return resumo


def gerar_contexto_llm(df):
    """
    Contexto enviado ao Gemini.
    """

    contexto = f"""
    Dataset com {df.shape[0]} linhas
    e {df.shape[1]} colunas.

    Colunas:
    {list(df.columns)}

    Primeiras linhas:
    {df.head(10).to_string()}
    """

    return contexto