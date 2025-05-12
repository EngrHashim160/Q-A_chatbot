import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()


## Langsmit Tracking
os.environ["LANGCHAIN_TRACING"] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot"

# Create prompt template
prompt = ChatPromptTemplate(
     [
         ("system", "You are a helpful assistant. Please answer the following question."),
         ("human", "{question}"),
     ]
)

# create parser object
parser = StrOutputParser()

def generate_response(question, api_key, llm, temperature, max_tokens):
    chain = prompt | llm | parser
    response = chain.invoke({"question": question})
    return response


# Title of the app
st.title("Enhanced Q&A Chatbot")    

# Sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your API key", type="password")

# Drop down for model selection (List of models that exists)
model_options = ["gemma2-9b-it", "llama3-70b-8192", "llama3-8b-8192", "llama-3.1-8b-instant", "llama-3.3-70b-versatile"]
selected_model = st.sidebar.selectbox("Select a model", model_options)

# Slider for temperature
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)

# Slider for max tokens
max_tokens = st.sidebar.slider("Max Tokens", 10, 1000, 200)

# Text input for question
question = st.text_input("Enter your question")

# Button to generate response
if st.button("Generate Response"):
    llm = ChatGroq(model=selected_model)
    response = generate_response(question, api_key, llm, temperature, max_tokens)
    st.write(response)  

