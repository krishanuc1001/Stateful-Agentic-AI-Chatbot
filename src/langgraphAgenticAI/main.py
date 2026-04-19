import streamlit as st
from src.langgraphAgenticAI.graph.graph_builder import GraphBuilder
from src.langgraphAgenticAI.llm.groq_llm import GroqLLM
from src.langgraphAgenticAI.llm.gemini_llm import GeminiLLM
from src.langgraphAgenticAI.ui.streamlit_ui.load_ui import LoadStreamlitUI
from src.langgraphAgenticAI.ui.streamlit_ui.display_result import DisplayResultStreamlit

def load_langgraph_agentic_app():
    """
    Loads the Streamlit UI for the Stateful Agentic AI Chatbot application. This function initializes the UI components,
    retrieves user selections, and returns them for use in the main application logic.
    """

    #Load UI
    ui=LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI. Please check the UI configuration and try again.")
        return
    
    """
    Text input handling and main application logic would go here. This includes:
    - Handling user input from the chat interface or other UI components.
    - Configuring the LLM based on user selections.
    - Building the appropriate graph based on the selected use case.
    - Executing the graph and displaying results on the UI.
    
    The implementation would include error handling to ensure a smooth user experience, 
    providing feedback in case of issues with input, configuration, or graph execution.
    """
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.time_frame
    else:
        user_message = st.chat_input("Enter your message here:")

    if user_message:
        
        try:
            # Check selected LLM provider
            selected_llm = user_input.get("selected_llm")
            
            if not selected_llm:
                st.error("Error: Please select an LLM provider to proceed.")
                return
            
            # Configure LLM based on selection
            if selected_llm == "Groq":
                object_llm_config = GroqLLM(user_controls_input=user_input)
            elif selected_llm == "Gemini":
                object_llm_config = GeminiLLM(user_controls_input=user_input)
            else:
                st.error(f"Error: Unsupported LLM provider: {selected_llm}")
                return
            
            model = object_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM configuration failed. Please check your selections and API keys.")
                return
            
            # Get the use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: Please select a use case to proceed.")
                return
            
            # Graph building and agentic logic would go here
            graph_builder = GraphBuilder(model=model)

            try:
                graph_builder.setup_graph(usecase)
                graph = graph_builder.graph_builder.compile()
                DisplayResultStreamlit(usecase=usecase, graph=graph, user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed: {e}")
                return

        except Exception as e:
            st.error(f"Error: Configuring LLM failed: {e}")
            return