import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            gemini_api_key = self.user_controls_input.get("GEMINI_API_KEY")
            selected_gemini_model = self.user_controls_input.get("selected_gemini_model")

            if not gemini_api_key:
                st.error("GEMINI API Key is required for Gemini LLM. Please enter it in the sidebar to proceed.")
                return None
            
            llm = ChatGoogleGenerativeAI(model=selected_gemini_model, api_key=gemini_api_key)

        except Exception as e:
            raise ValueError(f"Error configuring Gemini LLM: {e}")
        
        return llm