import streamlit as st
import json
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            for event in graph.stream({'messages': ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value['messages'].content)

        elif usecase == "Chatbot with Web Search Tool":
            initial_state = {'messages': [user_message]}
            response = graph.invoke(initial_state)
            for message in response['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("tool"):
                        st.write("Tool Call Started")
                        st.write(f"Tool Output: {message.content}")
                        st.write("Tool Call Ended")
                elif type(message) == AIMessage and message.content != "":
                    with st.chat_message("assistant"):
                        st.write(message.content)

        elif usecase == "AI News Summarizer":
            frequency = self.user_message
            with st.spinner('Fetching and summarizing news articles...  ⏳'):
                result = graph.invoke({'frequency': frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency}_summary.md"
                    with open(AI_NEWS_PATH, 'r') as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"Error: AI News Summary file not found: '{AI_NEWS_PATH}'. Please ensure the graph executed correctly and the file was created.")
                except Exception as e:
                    st.error(f"An unexpected error occurred while loading the AI News Summary: {e}")   