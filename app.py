import streamlit as st
import os
from dotenv import load_dotenv
from main import run_pulse_audit

load_dotenv()

st.set_page_config(page_title="Pulse-Audit", page_icon="📈", layout="wide")

st.title("📈 Pulse-Audit")
st.markdown("**Agentic Financial Intelligence & Compliance Auditing**")
st.markdown("Powered by **CrewAI** & **GPT-4o-mini**")

st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY", ""))

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
else:
    st.sidebar.warning("Please enter your OpenAI API Key")

st.subheader("Start New Audit")

col1, col2 = st.columns(2)
with col1:
    company_name = st.text_input("Company Name", "NVIDIA")
with col2:
    ticker = st.text_input("Ticker Symbol", "NVDA")

if st.button("Run Financial Audit"):
    if not api_key:
        st.error("API Key is required to run the audit.")
    else:
        with st.spinner(f"Agents are researching and analyzing {company_name} ({ticker})... This may take a few minutes."):
            try:
                report = run_pulse_audit(company_name, ticker)
                st.success("Audit Complete!")

                st.markdown("### 📋 Final Audit Report")
                st.markdown(report.raw)

                st.download_button(
                    label="Download Report as Markdown",
                    data=report.raw,
                    file_name=f"{ticker}_audit_report.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"An error occurred during execution: {e}")
