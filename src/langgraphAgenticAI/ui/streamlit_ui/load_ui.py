import streamlit as st
import os

from src.langgraphAgenticAI.ui.ui_config_reader import UIConfigReader

class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfigReader()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            #Get options from config and display in sidebar
            llm_options = self.config.get_lmm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                #Model Selection for Groq
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                #Show info if API Key is empty
                if not self.user_controls["GROQ_API_KEY"]:
                    st.info("Please enter your GROQ API Key to proceed. Get it from https://groq.com/")

            
            # Use Case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options)


        return self.user_controls
        
        
        # llm_options = self.config.get_llm_options()
        # if llm_options:
        #     st.subheader("Select LLM")
        #     selected_llm = st.selectbox("Choose a Language Model", llm_options)

        # # Load Use Case options
        # usecase_options = self.config.get_usecase_options()
        # if usecase_options:
        #     st.subheader("Select Use Case")
        #     selected_usecase = st.selectbox("Choose a Use Case", usecase_options)

        # # Load GROQ Model options
        # groq_model_options = self.config.get_groq_model_options()
        # if groq_model_options:
        #     st.subheader("Select GROQ Model")
        #     selected_groq_model = st.selectbox("Choose a GROQ Model", groq_model_options)
