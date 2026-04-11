from src.langgraphAgenticAI.state.state import State

class ChatbotWithWebSearchNode:
    """
    Chatbot with Web Search Tool Node that processes user input, 
    performs web search using the Tavily API, and generates a response using a specified LLM model.
    """

    def __init__(self, llm_model, tavily_api_key):
        self.llm_model = llm_model
        self.tavily_api_key = tavily_api_key

    def process(self, state: State) -> dict:
        """
        Processes the user input from the state, performs web search using the Tavily API, 
        generates a response using the LLM model, and returns the response.
        """

        # Get the latest user message
        user_input = state['messages'][-1] if state['messages'] else "" 
        llm_response = self.llm_model.invoke([{"role": "user", "content": user_input}]) 

        # Simulate tool sprcific logic to extract search query from LLM response and perform web search using Tavily API

        tools_response = f"Tool integration for: {user_input}"

        return {"messages": llm_response, "tools_response": tools_response}
    
    def create_chatbot(self, tools):
        """
        Factory method to create a chatbot instance with the specified tools.
        """
        llm_wih_tools = self.llm_model.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot node that processes user input, performs web search using the Tavily API, 
            and generates a response using the LLM model with tool integration.
            """
            return {"messages": [llm_wih_tools.invoke(state['messages'])]}
        
        return chatbot_node