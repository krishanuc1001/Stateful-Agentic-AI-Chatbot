from langgraph.graph import StateGraph, START, END
from src.langgraphAgenticAI.state.state import State
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode

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

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case. Currently, it supports a 'Basic Chatbot' use case, which constructs a simple conversational graph.
        The method checks the provided use case and calls the corresponding graph construction method. If an unsupported use case is provided, it raises a ValueError.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")