import pandas as pd


def identificar_colunas_numericas(df):
    return df.select_dtypes(include="number").columns.tolist()


def identificar_colunas_categoricas(df):
    return df.select_dtypes(exclude="number").columns.tolist()