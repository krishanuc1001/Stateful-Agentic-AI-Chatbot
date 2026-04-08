from typing_extensions import TypedDict, List
from typing import Annotated
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represents the state of the agentic AI chatbot used in Graph
    """

    messages: Annotated[List, add_messages]


