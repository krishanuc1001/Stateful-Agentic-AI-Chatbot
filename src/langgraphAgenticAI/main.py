import streamlit as st
from src.langgraphAgenticAI.graph.graph_builder import GraphBuilder
from src.langgraphAgenticAI.llm.groq_llm import GroqLLM
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
        
        try:
            # Configure LLM
            object_llm_config = GroqLLM(user_controls_input=user_input)
            model = object_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM configuration failed. Please check your selections and API keys.")
                return
            
            # Initialize the LLM with the configured model and API key
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: Please select a use case to proceed.")
                return
            
            # Graph building and agentic logic would go here, using the 'model' and 'usecase' variables as needed
            graph_builder = GraphBuilder(model=model, usecase=usecase)

            try:
                response = graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error(f"Error: Graph set up failed: {e}")
                return

        except Exception as e:

            st.error(f"Error configuring LLM: {e}")
            return None