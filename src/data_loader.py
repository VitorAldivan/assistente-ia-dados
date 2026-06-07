import pandas as pd


def carregar_arquivo(uploaded_file):
    """
    Carrega CSV ou XLSX.
    """

    nome = uploaded_file.name.lower()

    if nome.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if nome.endswith(".xlsx"):
        return pd.read_excel(uploaded_file)

    raise ValueError("Formato não suportado.")