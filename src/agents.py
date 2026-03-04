from crewai import Agent
from src.tools import search_internet, get_stock_data

def get_agents(llm=None):
    researcher = Agent(
        role='Senior Financial Researcher',
        goal='Gather comprehensive financial data and recent news about a target company.',
        backstory='You are an elite financial researcher working for a top-tier quantitative hedge fund. You excel at finding hidden gems and risks in financial reports and market news.',
        verbose=True,
        allow_delegation=False,
        tools=[search_internet, get_stock_data],
        llm=llm
    )

    analyst = Agent(
        role='Quantitative Financial Analyst',
        goal='Analyze the gathered data to evaluate the company\\'s financial health and market position.',
        backstory='With a PhD in Financial Mathematics, you have a keen eye for numbers. You can quickly understand valuations, growth prospects, and potential red flags.',
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=llm
    )

    auditor = Agent(
        role='Principal Compliance & Risk Auditor',
        goal='Synthesize research and analysis into a comprehensive, professional audit report.',
        backstory='You have 20 years of experience as a Big 4 auditor. You produce clear, highly structured markdown reports that executives rely on for billion-dollar decisions.',
        verbose=True,
        allow_delegation=False,
        tools=[],
        llm=llm
    )

    return researcher, analyst, auditor
