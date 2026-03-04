# 📈 Pulse-Audit: Agentic Financial Intelligence

Pulse-Audit is a multi-agent financial auditing platform powered by CrewAI and GPT-4o. It orchestrates specialized AI agents (Researcher, Quantitative Analyst, and Compliance Auditor) to automatically gather real-time market data, analyze financial health, and produce comprehensive audit reports.

## Features
- **Multi-Agent Orchestration**: Specialized roles for research, analysis, and reporting.
- **Real-Time Data**: Integrates with Yahoo Finance and DuckDuckGo for live market data and news.
- **Premium UI**: Easy-to-use Streamlit dashboard for initiating audits and downloading reports.
- **Markdown Export**: Generates professional, ready-to-present markdown reports.

## 🛠 Setup & Installation

1. **Clone the repository** (or download the source code).
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up Environment Variables**:
   Copy `.env.example` to `.env` and add your OpenAI API Key:
   ```bash
   cp .env.example .env
   ```

## 🚀 Usage

### Streamlit Dashboard (Recommended)
Launch the interactive web application:
```bash
streamlit run app.py
```

### CLI Execution
Run the orchestrator directly from the terminal for testing:
```bash
python main.py
```

## Architecture
- `src/agents.py`: Defines the Researcher, Analyst, and Auditor agents.
- `src/tasks.py`: Defines the sequence of tasks for the Crew.
- `src/tools.py`: Custom Langchain tools for fetching stock data and web searches.
- `main.py`: CrewAI process orchestration.
- `app.py`: Streamlit frontend.
