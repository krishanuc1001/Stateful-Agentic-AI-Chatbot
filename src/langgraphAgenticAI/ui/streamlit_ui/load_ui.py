import streamlit as st
import os

from src.langgraphAgenticAI.ui.ui_config_reader import UIConfigReader

class LoadStreamlitUI:
    def __init__(self):
        self.config = UIConfigReader()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(" 🤖 " + self.config.get_page_title())
        st.session_state.IsFetchButtonClicked = False
        st.session_state.time_frame = ""


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

            elif self.user_controls["selected_llm"] == "Gemini":

                #Model Selection for Gemini
                model_options = self.config.get_gemini_model_options()
                self.user_controls["selected_gemini_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GEMINI_API_KEY"] = st.session_state["GEMINI_API_KEY"] = st.text_input("API Key", type="password")

                #Show info if API Key is empty
                if not self.user_controls["GEMINI_API_KEY"]:
                    st.info("Please enter your GEMINI API Key to proceed. Get it from https://ai.google.com/")

            # Use Case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web Search Tool" or self.user_controls["selected_usecase"] == "AI News Summarizer":
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API Key for Web Search Tool", type="password")
                
                # Validate Tavily API Key input
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your Tavily API Key to use the Web Search Tool. Get it from https://app.tavily.com/home")

            if self.user_controls['selected_usecase'] == "AI News Summarizer":
                st.subheader("📰 AI News Summarizer")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "🗓️ Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index = 0
                    )

                if st.button("🔎  Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.time_frame = time_frame

        return self.user_controls
