# Chatbot no navegador
Um chatbot desenvolvido com LLM implementado com Langchain e Streamlit para interface no navegador

# Pré-requisitos

Python 3.9+

> ## Bibliotecas

[Streamlit](https://docs.streamlit.io)

[Langchain](https://python.langchain.com/docs/introduction/)

Dotenv

#### Faça a instalação do ambiente virtual via terminal
    python -m venv env
    .\env\Scripts\activate

#### Instale as bibliotecas
utilizei a model de IA Groq por isso baixei o pacote correspondente do langchain, no arquivo `.env` adicione sua chave de api

    pip install streamlit langchain langchain[groq] python-dotenv

# Uso
> ## No terminal, execute o comando `streamlit run main.py`
