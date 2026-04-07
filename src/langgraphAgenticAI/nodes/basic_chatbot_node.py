from src.langgraphAgenticAI.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot Node that processes user input and generates a response using a specified LLM model.
    """

    def __init__(self, llm_model):
        self.llm_model = llm_model

    def process(self, state: State) -> dict:
        """
        Processes the user input from the state, generates a response using the LLM model, and returns the response.
        """

        return {"messages": self.llm_model.invoke(state['messages'])}