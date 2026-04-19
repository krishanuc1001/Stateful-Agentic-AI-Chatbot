from langgraph.graph import StateGraph, START, END
from src.langgraphAgenticAI.state.state import State
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphAgenticAI.tools.search_tool import get_tools, create_tool_nodes
from langgraph.prebuilt import tools_condition, ToolNode
from src.langgraphAgenticAI.nodes.chatbot_with_websearch_node import ChatbotWithWebSearchNode
import os

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

    def chatbot_with_web_search_graph(self):
        """
        Builds a graph for a chatbot use case that includes a web search tool.
        This method creates a Chatbot graph that includes both the chatbot node and the web search tool node, integrating them into the graph structure.
        It defines tools, initializes the chatbot node with the necessary tools, and sets up the edges to allow for a dynamic conversational flow where the chatbot can utilize the web search tool as needed.
        The Chatbot node is set as the Entry point of the graph, and the Web Search Tool node is connected to the chatbot node, allowing for interactions between the two. 
        The Web Search Tool node is also connected to the Exit point of the graph, enabling a complete flow from user input to final response.
        The flow allows the chatbot to utilize the web search tool as needed during the conversation, providing a more dynamic and informative user experience.
        """

        # Define the tool and tool node
        tools = get_tools()
        tool_node = create_tool_nodes(tools)

        # Define the LLM
        llm = self.llm

        #Define the chatbot node with the tool
        tavily_api_key = os.environ["TAVILY_API_KEY"]
        obj_chatbot_with_node = ChatbotWithWebSearchNode(llm, tavily_api_key)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)
        
        # Add nodes and edges to the graph
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define conditional and direct edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def ai_news_summarizer_graph(self):
        """
        Builds a graph for an AI news summarizer use case.
        This method creates a graph that includes nodes for fetching news articles, summarizing them, and providing the summarized output to the user.
        It defines the necessary tools and integrates them into the graph structure, allowing for a dynamic flow where the AI can fetch and summarize news articles based on user input.
        The flow starts with the user input, which triggers the news fetching node. The fetched news articles are then passed to the summarization node, which processes the information and provides a concise summary back to the user.
        This setup allows for an efficient and informative user experience when interacting with the AI news summarizer.
        """

        # Added Nodes
        self.graph_builder.add_node("fetch_news", "")
        self.graph_builder.add_node("summarize_news", "")
        self.graph_builder.add_edge("save_result", "")

        # Added Edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_result")
        self.graph_builder.set_exit_point("save_result")

    
    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case. Currently, it supports a 'Basic Chatbot' use case, which constructs a simple conversational graph.
        The method checks the provided use case and calls the corresponding graph construction method. If an unsupported use case is provided, it raises a ValueError.
        """

        if usecase == "Basic Chatbot":
            self.basic_chatbot_graph()
        elif usecase == "Chatbot with Web Search Tool":
            self.chatbot_with_web_search_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")
        return self.graph_builder.compile()