import google.generativeai as genai

from src.config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

modelo = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)


def perguntar_dados(pergunta, contexto):
    """
    Faz perguntas sobre o dataframe.
    """

    prompt = f"""
    Você é um analista de dados.

    Contexto:

    {contexto}

    Pergunta:

    {pergunta}

    Responda de forma objetiva,
    utilizando apenas informações
    presentes no dataset.
    """

    resposta = modelo.generate_content(prompt)

    return resposta.text