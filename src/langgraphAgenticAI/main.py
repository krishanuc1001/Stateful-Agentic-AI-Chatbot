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

    # Display chat input regardless of form completion
    user_message = st.chat_input("Enter your message here:")

    if user_message:
        # Validate user_input is available
        if not user_input:
            st.error("Please complete the sidebar configuration to proceed.")
            return None
        
        # Check if API key is provided (if using Groq)
        if user_input.get("selected_llm") == "Groq" and not user_input.get("GROQ_API_KEY"):
            st.error("Please enter your GROQ API Key in the sidebar to proceed.")
            return None

        # try:
            #Configure LLM
            # object_llm_config = GroqLLM(user_controls_input=user_input)
            # model = object_llm_config.get_llm_model()

            # if not model:
            #     st.warning("LLM model configuration is incomplete. Please check your selections and try again.")
            #     return
            
            #Initialize and Setup the Graph based on Use Case
            # usecase = user_input.get("selected_usecase")
            # if not usecase:
            #     st.warning("Use case selection is required. Please select a use case from the sidebar.")
            #     return
        #     usecase = user_input.get("selected_usecase")
        #     if not usecase:
        #         st.warning("Use case selection is required. Please select a use case from the sidebar.")
        #         return