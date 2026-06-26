import streamlit as st
import pandas as pd
import plotly.express as px
from utils.ui import apply_style, sidebar
from data.projects import PROJECTS
import streamlit as st
from pathlib import Path

# ============================================================
# Header Image
# ============================================================

assets_path = Path(__file__).resolve().parents[1] / "assets"

def show_header(image_name):
    st.image(
        str(assets_path / image_name),
        use_container_width=True
    )

show_header("risk_header.png")

# ============================================================



st.set_page_config(page_title="Market Risk Analytics", page_icon="⚠️", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='risk')

#st.image(p['banner'], use_container_width=True)
st.title("Market Volatility, VaR & Stress Testing")
st.caption("Portfolio risk analytics across S&P 500, Gold, and Oil")
cols = st.columns(4)
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

left, right = st.columns([1.1,.9])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Business translation:</b> {p["business_value"]}</p></div>', unsafe_allow_html=True)
    stress = pd.DataFrame({"Scenario":["Equity Market Crash", "Global Recession", "Inflation Shock", "Commodity Spike"], "Portfolio Return":[-11.5,-10.0,-4.8,2.9]})
    fig = px.bar(stress, x="Scenario", y="Portfolio Return", text="Portfolio Return", template="plotly_dark", title="Portfolio Return Under Stress Scenarios")
    fig.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white")
    st.plotly_chart(fig, use_container_width=True)
with right:
    summary = pd.DataFrame({
        "Component":["Volatility Forecasting", "VaR Forecasting", "Stress Testing"],
        "Method":["SARIMA + Auto ARIMA", "SARIMA + Auto ARIMA", "Scenario Analysis"],
        "Business Value":["Detect future risk build-up", "Estimate downside loss", "Assess resilience under shocks"]
    })
    st.markdown("### Executive risk components")
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)
