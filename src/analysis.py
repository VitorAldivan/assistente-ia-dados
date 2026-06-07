import pandas as pd


def gerar_resumo(df):
    return {
        "linhas": df.shape[0],
        "colunas": df.shape[1],
        "nomes_colunas": list(df.columns),
        "nulos": df.isnull().sum().to_dict(),
    }


def gerar_contexto_llm(df):

    contexto = f"""
    DATASET COMPLETO

    Total de linhas: {df.shape[0]}
    Total de colunas: {df.shape[1]}

    Colunas:
    {list(df.columns)}

    Tipos:
    {df.dtypes.to_string()}

    Valores nulos:
    {df.isnull().sum().to_string()}

    DADOS:
    """

    
    contexto += "\n"
    contexto += df.to_csv(index=False)

    return contexto