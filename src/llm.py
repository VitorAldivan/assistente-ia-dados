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
Sempre comece a resposta com o valor pedido por quem está fazendo a pergunta, sem rodeios. ou seja, se a pergunta for "Qual produto vendeu mais?", a resposta deve começar com o nome do produto que vendeu mais, seguido de uma breve explicação.

    - Não invente informações.
    - Se não houver dados suficientes,
      informe isso.
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