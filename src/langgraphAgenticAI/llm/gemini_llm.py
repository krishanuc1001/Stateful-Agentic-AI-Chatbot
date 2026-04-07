import os
import streamlit as st
from langchain_gemini import ChatGemini

class GeminiLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            gemini_api_key = self.user_controls_input.get["GEMINI_API_KEY"]
            selected_gemini_model = self.user_controls_input["selected_gemini_model"]

            if gemini_api_key == '' and os.environ["GEMINI_API_KEY"] == '':
                st.error("GEMINI API Key is required for Gemini LLM. Please enter it in the sidebar to proceed.")
            

            llm = ChatGemini(model=selected_gemini_model, api_key=gemini_api_key)

        except Exception as e:
            raise ValueError(f"Error configuring Gemini LLM: {e}")
        
        return llm