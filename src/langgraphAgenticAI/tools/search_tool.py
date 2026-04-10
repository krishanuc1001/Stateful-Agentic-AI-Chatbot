from langchain_community.tools.tavily_search import TavilySearchResults, TavilySearchTool
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tools to be used in the chatbot graph. 
    Currently, it includes the 'TavilySearchResults' tool, which allows the chatbot to perform web searches
    and retrieve relevant information from the internet.
    """

    tools = [TavilySearchResults(max_results=2)]
    return tools 

def create_tool_nodes(tools):
    """
    Creates and returns a list of ToolNode instances based on the provided tools. Each tool is wrapped in a ToolNode, which allows it to be integrated into the graph structure and utilized by the chatbot during conversations.
    The function iterates through the list of tools, creates a corresponding ToolNode for each tool, and collects them into a list that can be returned for use in the graph construction.
    """

    return ToolNode(tools=tools)
