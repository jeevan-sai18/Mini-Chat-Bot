from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ai21 import AI21
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from constants import ai21_key


st.set_page_config(page_title="Chat Bot", page_icon="🤖")

# Set the API key
os.environ["AI21_API_KEY"] = ai21_key

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.Please respond to the user queries"),
        ("user","Question:{question}")
    ]

)

#streamlit framework

st.title('Mini Chat Bot')
input_text=st.text_input("Search the topic you want")

llm=AI21(model="j2-large")
output_parser=StrOutputParser()

#chain
chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))