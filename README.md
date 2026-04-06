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

| Component          | Technology                                           |
| ------------------ | ---------------------------------------------------- |
| **LLM**            | Llama 3 (via Groq - High-speed inference)            |
| **Orchestration**  | LangGraph (Cyclical workflows with persistent state) |
| **Web Framework**  | Streamlit (Interactive UI)                           |
| **Language**       | Python 3.9+                                          |
| **Core Libraries** | LangChain, LangChain Community, LangChain Groq       |
| **API Clients**    | Groq API, OpenAI API (optional)                      |
| **Utilities**      | Tavily Python (for information retrieval)            |

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

### Running the Streamlit UI Locally

1. **Ensure you're in the project directory**

   ```bash
   cd Stateful_Agentic_AI
   ```

2. **Activate the virtual environment** (if not already activated)

   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Start the Streamlit application**

   ```bash
   streamlit run app.py
   ```

4. **Access the UI**
   - The application will automatically open in your default browser at `http://localhost:8501`
   - If it doesn't open automatically, manually navigate to `http://localhost:8501`

### First-Time Setup in the UI

1. **Select LLM Provider** (Sidebar)
   - Choose "Groq" to use Llama 3 models

2. **Enter Groq API Key** (Sidebar)
   - Get your API key from https://groq.com/
   - Paste it in the "API Key" field

3. **Select Model** (Sidebar)
   - Choose your preferred Llama model (e.g., llama3-8b-8192)

4. **Select Use Case** (Sidebar)
   - Pick the use case relevant to your needs

5. **Start Interacting**
   - Begin your conversation with the AI assistant in the main chat area

### Interacting with the System

- **Conversational Chatbot** - Have natural language conversations with context awareness
- **Agentic Capabilities** - Request the agent to perform specific tasks using integrated tools
- **State Persistence** - Your conversation history is maintained across interactions

## Project Structure

```
Stateful_Agentic_AI/
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
├── .gitignore               # Git ignore rules
├── app.py                   # Entry point for Streamlit application
├── .env                     # Environment variables (not in git)
│
├── src/
│   ├── __init__.py
│   └── langgraphAgenticAI/
│       ├── __init__.py
│       ├── main.py                    # Main application logic
│       ├── graph/                     # LangGraph workflow definitions
│       │   └── __init__.py
│       ├── llm/                       # LLM configurations
│       │   └── __init__.py
│       ├── nodes/                     # Graph node implementations
│       │   └── __init__.py
│       ├── state/                     # State management
│       │   └── __init__.py
│       ├── tools/                     # Tool integrations
│       │   └── __init__.py
│       └── ui/                        # User interface layer
│           ├── __init__.py
│           ├── ui_config_reader.py    # Configuration reader
│           ├── ui_config.ini          # UI configuration file
│           └── streamlit_ui/
│               ├── __init__.py
│               ├── load_ui.py         # Streamlit UI loader
│               └── display_ui.py      # UI display components
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

## Troubleshooting

### Port Already in Use

If port 8501 is already in use, you can specify a different port:

```bash
streamlit run app.py --server.port 8502
```

### API Key Issues

- Ensure your Groq API key is valid and not expired
- API key should be entered in the Streamlit sidebar before starting
- Check that you have sufficient credit/quota on your Groq account

### Environment Variables

If you want to use environment variables instead of entering the API key in the UI:

```bash
export GROQ_API_KEY=your_groq_api_key
streamlit run app.py
```

---

**Status**: 🚀 Active Development

**Last Updated**: April 2026
