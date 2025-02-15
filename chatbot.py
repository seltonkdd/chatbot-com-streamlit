from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
        ('system', '''Você é um assistente virtual, ajude o usúario respondendo perguntas. Responda sempre em português.'''),
        MessagesPlaceholder('chat_history', optional=True),
        MessagesPlaceholder('msgs')
    ])

list = []

def call_model():

    message_input = input('\nVocê: ')
    list.append(message_input)
    prompt = prompt_template.invoke({'msgs': list})

    response = llm.invoke(prompt)
    print(response.content)

