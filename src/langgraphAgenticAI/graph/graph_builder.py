from langgraph.graph import StateGraph, START, END
from src.langgraphAgenticAI.state.state import State

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_graph(self):
        """
        Builds a simple graph for a basic chatbot use case.
        This method initializes a Chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph structure. The Chatbot node is set as both the Entry and Exit point of the graph, 
        allowing for a straightforward conversational flow.
        """

        self.graph_builder.add_node("chatbot", "")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)