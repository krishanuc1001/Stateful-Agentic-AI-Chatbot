import streamlit as st
from src.langgraphAgenticAI.ui.streamlit_ui.load_ui import LoadStreamlitUI

def load_langgraph_agentic_app():
    """
    Loads the Streamlit UI for the Stateful Agentic AI Chatbot application. This function initializes the UI components,
    retrieves user selections, and returns them for use in the main application logic.
    """

    #Load UI
    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.warning("Please make the necessary selections in the sidebar to proceed.")
        return None
    
    user_message = st.chat_input("Enter your message here:")

    # if user_message:
        # try:
        #     #Configure LLM
        #     object_llm_config = GroqLLM(user_controls_input=user_input)
        #     model = object_llm_config.get_llm_model()

        #     if not model:
        #         st.warning("LLM model configuration is incomplete. Please check your selections and try again.")
        #         return
            
        #     #Initialize and Setup the Graph based on Use Case
        #     usecase = user_input.get("selected_usecase")
        #     if not usecase:
        #         st.warning("Use case selection is required. Please select a use case from the sidebar.")
        #         return