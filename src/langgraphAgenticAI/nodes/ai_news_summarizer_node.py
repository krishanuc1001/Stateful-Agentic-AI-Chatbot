from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

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

        frequency = state['messages'][0].content.lower() if state.get('messages') else "daily"
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

    def summarize_news(self, state: dict) -> dict:
        """
        Summarizes the fetched news articles using the language model (LLM) and updates the state with the summarized news.
        
        Args:
            state (dict): The state dictionary that contains the fetched news data under the key 'news_data'. 
            This data is used to generate a summary of the news articles.

        Returns:
            dict: Updated state with "summary" key containing the summarized news.
        """

        news_items = self.state.get('news_data', [])
        
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """Summarize AI news articles into markdown format. For each item include:
            - Date in **YYYY-MM-DD** format in IST timezone
            - Concise sentences summary from latest news
            - Sort news by date wise (latest first)
            - Source URL as link
            Use format:
            ### [Date]
            - [Summary](URL)"""),
            ("user", "Articles:\n{articles}")
        ])

        articles_str = "\n\n".join([
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        ])

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state
    
    def save_result(self,state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency}_summary.md"
        
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        
        self.state['filename'] = filename
        return self.state
        
        