from tavily import TavilyClient
from langgchain_core.prompts import ChatPromptTemplate

class AINewsSummarizerNode:

    def __init__(self, llm):
        """
        Initializes the AINewsSummarizerNode with a language model (LLM) and sets up the Tavily client for news summarization.
        """
        self.tavily = TavilyClient()
        self.llm = llm

        """
        Initialize the state for the node, which can be used to store intermediate data or results 
        during the processing of news articles and summarization.
        """  
        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetches news articles based on the specified frequency and updates the state with the fetched news data.
        
        Args:
            state (dict): The current state of the node, which may contain parameters for fetching news (e.g., frequency).

        Returns:
            dict: Updated state containing the news_data.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {
            "daily": "d",
            "weekly": "w",
            "monthly": "m",
            "yearly": "y"
        }
        days_map = {
            "daily": 1,
            "weekly": 7,
            "monthly": 30,
            "yearly": 365
        }
        
        response = self.tavily.search(
            query="Top Artificial Intelligence technology news India and globally",
            topic = "news",
            time_range = time_range_map[frequency],
            include_answer = "advanced",
            max_results = 20,
            days = days_map[frequency],
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        return state

        
        