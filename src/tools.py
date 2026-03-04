from langchain_core.tools import tool
import yfinance as yf
from duckduckgo_search import DDGS

@tool("Search Internet")
def search_internet(query: str) -> str:
    """Search the internet for news and information."""
    try:
        results = DDGS().text(query, max_results=5)
        if results:
            return "\n".join([f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}" for r in results])
        return "No results found."
    except Exception as e:
        return f"Error searching internet: {e}"

@tool("Get Stock Data")
def get_stock_data(ticker: str) -> str:
    """Get recent stock data and financial ratios for a given ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return f"Current Price: {info.get('currentPrice', 'N/A')}\nMarket Cap: {info.get('marketCap', 'N/A')}\nP/E Ratio: {info.get('trailingPE', 'N/A')}\nForward P/E: {info.get('forwardPE', 'N/A')}\nDebt to Equity: {info.get('debtToEquity', 'N/A')}"
    except Exception as e:
        return f"Error fetching stock data: {e}"
