from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
        ('system', '''Você é um assistente virtual, ajude o usúario respondendo perguntas. Responda sempre em português.'''),
        MessagesPlaceholder('chat_history', optional=True),
        ('human', '{last_message}')
    ])

list = []

def call_model(message_input):

    list.append({'role': 'user', 'content': message_input})
    prompt = prompt_template.invoke({'chat_history': list[:-1], 'last_message': message_input})

    response = llm.invoke(prompt)
    list.append({'role': 'assistant', 'content': response.content})

    return response.content, list

