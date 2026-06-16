# 🤖 Assistente IA para Análise de Dados

## 📌 Sobre o Projeto

Este projeto consiste em um assistente inteligente para análise de dados desenvolvido com Python, Streamlit e Google Gemini.

A aplicação permite que o usuário faça upload de arquivos CSV ou Excel, visualize os dados carregados e realize perguntas em linguagem natural sobre o dataset.

O objetivo do projeto é demonstrar conhecimentos em análise de dados, manipulação de datasets com Pandas, integração com APIs de Inteligência Artificial, desenvolvimento de aplicações web e boas práticas de organização de projetos Python.

---

## 🚀 Tecnologias Utilizadas

* Python
* Pandas
* Streamlit
* Google Gemini API
* OpenPyXL
* Python Dotenv
* Git
* GitHub

---

## 📂 Estrutura do Projeto

```text
assistente-ia-dados/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── exploracao.ipynb
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── config.py
│   ├── data_loader.py
│   ├── llm.py
│   └── utils.py
│
├── tests/
│   └── test_data_loader.py
│
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## ⚙️ Funcionalidades

* Upload de arquivos CSV
* Upload de arquivos Excel (.xlsx)
* Visualização completa dos dados carregados
* Identificação automática de linhas e colunas
* Contagem de valores nulos
* Processamento de dados com Pandas
* Integração com Inteligência Artificial (Gemini)
* Consultas em linguagem natural
* Interface web interativa com Streamlit

---

## 📊 Informações Exibidas

O sistema apresenta automaticamente:

* Quantidade de linhas
* Quantidade de colunas
* Quantidade de valores nulos
* Visualização completa do dataset
* Estrutura dos dados enviados pelo usuário

---

## 🤖 Exemplos de Perguntas

Após carregar um arquivo, o usuário pode realizar perguntas como:

* Qual produto possui mais vendas?
* Qual região apresentou melhor desempenho?
* Qual é a média da coluna de faturamento?
* Existem registros duplicados?
* Há valores nulos no dataset?
* Quais são os principais insights encontrados?
* Qual cliente realizou mais compras?

---

## ▶️ Como Executar

### Clone o repositório

```bash
git clone https://github.com/VitorAldivan/assistente-ia-dados.git
```

### Acesse a pasta do projeto

```bash
cd assistente-ia-dados
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Configure a chave da API Gemini

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

### Execute a aplicação

```bash
python -m streamlit run app/streamlit_app.py
```

---

## ⚠️ Limitações da Versão Gratuita da IA

Este projeto utiliza a API Gemini para responder perguntas sobre os dados enviados pelo usuário.

A versão gratuita da API possui limitações de:

* Quantidade de requisições por minuto
* Quantidade de tokens processados por minuto
* Volume de dados enviados para análise

Durante o uso intenso ou ao analisar datasets muito grandes, podem ocorrer mensagens de limite excedido (Quota Exceeded).

Para utilização contínua, análise de grandes volumes de dados ou uso em ambiente de produção, recomenda-se utilizar uma chave com faturamento habilitado na plataforma Google AI Studio.

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido com foco em:

* Manipulação de dados com Pandas
* Desenvolvimento de aplicações web com Streamlit
* Integração com APIs de Inteligência Artificial
* Estruturação de projetos Python
* Versionamento com Git e GitHub
* Boas práticas de organização de código
* Construção de soluções voltadas para análise de dados

---

## 📷 Screenshots

### Tela Inicial

<img width="922" height="344" alt="image" src="https://github.com/user-attachments/assets/00f7f998-e525-494c-bdf5-aca7bc9206f7" />


### Upload de Dataset

<img width="923" height="389" alt="Captura de tela 2026-06-15 214829" src="https://github.com/user-attachments/assets/36d19218-7254-4069-9901-152fa5097bd7" />


### Pergunta para IA

<img width="916" height="215" alt="Captura de tela 2026-06-15 214855" src="https://github.com/user-attachments/assets/0b91082c-f132-4816-ae3a-c1bbade70fa7" />



### Resposta Gerada pela IA

<img width="921" height="263" alt="image" src="https://github.com/user-attachments/assets/f961fc1c-2364-433f-a71f-6570a3022a6d" />

---

## 👨‍💻 Autor

Desenvolvido como projeto de portfólio para estudos de Python, Análise de Dados, Inteligência Artificial e Desenvolvimento de Aplicações Data-Driven.
