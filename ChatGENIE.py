import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Set your API key (make sure it's safe to use this way or load from a secret manager)
load_dotenv()
gemini_api_key=os.getenv("GOOGLE_API_KEY")

# Streamlit UI
st.title("🔮 CHAT GENIE")
st.write("Welcome to ChatGenie 🧞 your problem-solving partner. What can I clarify for you?")
input_text = st.text_input("Ask me anything:")

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",api_key=gemini_api_key)

# Define a simple prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question:\n\nQuestion: {question}\nAnswer:"
)

# Set up the LLMChain
chain = LLMChain(llm=llm, prompt=prompt, verbose=False)

# Handle user input
if input_text.strip():
    try:
        # Run the chain with user input
        response = chain.run({"question": input_text})
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter a question to get started.")
