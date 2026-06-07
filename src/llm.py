import google.generativeai as genai

from src.config import GEMINI_API_KEY


genai.configure(api_key=GEMINI_API_KEY)

modelo = genai.GenerativeModel(
    model_name="gemini-2.5-flash"
)


def perguntar_dados(pergunta, contexto):

    prompt = f"""
    Você é um analista de dados sênior.

    Analise exclusivamente o dataset fornecido.

    Regras:

    - Não invente informações.
    - Se não houver dados suficientes,
      informe isso.
    - Explique sua resposta.
    - Utilize números quando possível.
    - Responda em português.

    CONTEXTO:

    {contexto}

    PERGUNTA:

    {pergunta}
    """

    resposta = modelo.generate_content(
        prompt
    )

    return resposta.text