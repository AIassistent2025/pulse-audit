import os
import sys
from dotenv import load_dotenv

# Workaround for chromadb crash on python 3.13 in crewai
import types
try:
    import chromadb
except Exception:
    sys.modules['chromadb'] = types.ModuleType('chromadb')

from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from src.agents import get_agents
from src.tasks import get_tasks

load_dotenv()

def run_pulse_audit(company_name: str, ticker: str):
    """
    Kicks off the multi-agent financial audit process.
    """
    print(f"[*] Starting Pulse-Audit for {company_name} ({ticker})...")
    
    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    
    # Get Agents
    researcher, analyst, auditor = get_agents(llm=llm)
    
    # Get Tasks
    research_task, analysis_task, writing_task = get_tasks(
        researcher, analyst, auditor, company_name, ticker
    )
    
    # Form the Crew
    audit_crew = Crew(
        agents=[researcher, analyst, auditor],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Execute
    result = audit_crew.kickoff()
    return result

if __name__ == "__main__":
    test_company = "NVIDIA"
    test_ticker = "NVDA"
    try:
        if not os.getenv("OPENAI_API_KEY"):
            print("[ERROR] OPENAI_API_KEY is missing from environment variables.")
        else:
            report = run_pulse_audit(test_company, test_ticker)
            print("\\n=== FINAL REPORT ===\\n")
            print(report)
    except Exception as e:
        print(f"[ERROR] Execution failed: {e}")
