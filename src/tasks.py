from crewai import Task

def get_tasks(researcher, analyst, auditor, company_name, ticker):
    research_task = Task(
        description=f'Search for the latest financial news, earnings reports, and stock data for {company_name} (Ticker: {ticker}). Extract key balance sheet and income statement figures, as well as current market sentiment.',
        expected_output='A detailed summary of raw financial data, stock metrics, and links to source documents.',
        agent=researcher
    )

    analysis_task = Task(
        description=f'Based on the research for {company_name}, analyze the P/E ratio, market cap, and recent news. Identify any growth opportunities, discrepancies, or potential red flags.',
        expected_output='A technical assessment of the company\\'s financial health and market position.',
        agent=analyst
    )

    writing_task = Task(
        description=f'Generate a final audit report for {company_name}. Include an Executive Summary, Financial Performance section, and a Risk Assessment based on the analyst\\'s findings.',
        expected_output='A professional markdown report titled "Financial Audit Report: {company_name}".',
        agent=auditor,
        context=[research_task, analysis_task]
    )

    return research_task, analysis_task, writing_task
