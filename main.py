from chatbot import call_model
import streamlit as st

st.title('Chatbot no navegador')

input_text = st.text_input('Digite sua mensagem')
if st.button('Enviar'):
    if input_text:
        ai_response = call_model(input_text)
        st.write(ai_response)
    else: 
        st.write('Escreva pelo menos uma mensagem')


