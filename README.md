# Stateful Agentic AI System using LangGraph and Llama 3

Building an AI-driven multi-agent system for intelligent orchestration, risk prediction, and decision-making across the Software Delivery Life Cycle (SDLC).

![LangGraph](https://img.shields.io/badge/LangGraph-Framework-blue)
![Llama 3](https://img.shields.io/badge/Llama-3-green)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)

## Table of Contents

- [Abstract](#abstract)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Abstract

### Background

Most traditional AI chatbot implementations are stateless, meaning they lack memory of previous interactions and fail to handle complex, multi-step workflows. This limitation significantly reduces their effectiveness in real-world applications where context, reasoning, and continuity are essential.

### Motivation

With the growing need for intelligent systems that can not only respond but also act, reason, and maintain context, there is strong demand for building agentic AI systems. This project bridges the gap between simple LLM-based applications and production-grade AI systems by introducing stateful, memory-aware workflows.

### Proposed Solution

This project develops a modular, stateful agentic AI system using LangGraph and Llama 3. The system consists of three key components:

1. **Conversational Chatbot** - Context-aware natural language interactions
2. **Tool-Augmented Agent** - Dynamic code generation and execution capabilities
3. **AI News Aggregator** - Real-time information retrieval and summarization

The architecture leverages:

- **LangGraph** for building cyclical workflows with persistent state
- **Groq** for high-performance inference
- **Streamlit** for interactive user interface
- Modular coding practices for scalability and maintainability

### Expected Outcomes

✅ Fully functional, stateful AI assistant with context-aware interactions  
✅ Demonstration of agentic behavior through tool usage and reasoning  
✅ Production-ready, modular codebase aligned with industry standards  
✅ Live, deployable application accessible via public URL  
✅ Comprehensive understanding of real-world AI system design and deployment

## Key Features

- **Stateful Conversations** - Persistent memory across multi-turn interactions
- **Multi-Agent Orchestration** - Intelligent routing and coordination between specialized agents
- **Tool Integration** - Dynamic tool execution with reasoning capabilities
- **Real-time Information** - Current news and data aggregation
- **Interactive UI** - User-friendly Streamlit interface
- **Modular Architecture** - Clean separation of concerns for maintainability
- **Production-Ready** - Industry-standard practices and deployment capabilities

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Streamlit UI Layer                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                   LangGraph State Manager                    │
│              (Handles persistence & routing)                │
└─────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
     ┌────────────┐  ┌────────────┐  ┌──────────────┐
     │  Chatbot   │  │   Agent    │  │News Aggreg.  │
     │  Component │  │ Component  │  │  Component   │
     └────────────┘  └────────────┘  └──────────────┘
            │               │               │
            └───────────────┼───────────────┘
                            ▼
        ┌─────────────────────────────────────┐
        │  Llama 3 (via Groq API)             │
        └─────────────────────────────────────┘
```

## Tech Stack

| Component           | Technology                                                       |
| ------------------- | ---------------------------------------------------------------- |
| **LLM**             | Llama 3 (via Groq)                                               |
| **Orchestration**   | LangGraph                                                        |
| **Vector Database** | FAISS                                                            |
| **Web Framework**   | Streamlit                                                        |
| **Language**        | Python 3.9+                                                      |
| **API Clients**     | LangChain, LangChain Community, LangChain Groq, LangChain OpenAI |
| **Utilities**       | Tavily Python                                                    |

## Installation

### Prerequisites

- Python 3.9 or higher
- pip or conda package manager
- Groq API key (for Llama 3 inference)
- Optional: OpenAI API key (for alternative LLM support)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Stateful_Agentic_AI.git
   cd Stateful_Agentic_AI
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_groq_api_key" > .env
   echo "OPENAI_API_KEY=your_openai_api_key" >> .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## Usage

### Starting the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

### Interacting with the System

1. **Chatbot Mode** - Start conversing with the AI assistant
2. **Agent Mode** - Request the agent to perform specific tasks
3. **News Mode** - Get aggregated AI and tech news summaries

## Project Structure

```
Stateful_Agentic_AI/
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
├── .gitignore               # Git ignore rules
├── app.py                   # Main Streamlit application
├── .env                     # Environment variables (not in git)
│
├── src/
│   ├── __init__.py
│   ├── chatbot.py           # Conversational component
│   ├── agent.py             # Tool-augmented agent
│   ├── news_aggregator.py   # News retrieval & summarization
│   ├── state_manager.py     # LangGraph state management
│   └── utils.py             # Helper functions
│
└── tests/
    ├── __init__.py
    ├── test_chatbot.py
    ├── test_agent.py
    └── test_news_aggregator.py
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Status**: 🚧 In Development

**Author**: [Your Name]  
**Last Updated**: April 2026
