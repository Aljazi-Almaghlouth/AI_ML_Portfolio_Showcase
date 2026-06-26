import streamlit as st
import pandas as pd
import numpy as np
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

show_header("nasdaq_header.png")

# ============================================================

st.set_page_config(page_title="Nasdaq Time-Series Forecasting", page_icon="📈", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='nasdaq')

#st.image(p['banner'], use_container_width=True)
st.title("Nasdaq Time-Series Decomposition & Forecasting")
st.caption("Decomposition with ETS · Forecasting with SARIMA and SARIMAX")
cols = st.columns(4)
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

np.random.seed(7)
dates = pd.date_range("2023-01-17", periods=60, freq="B")
trend = np.linspace(11095, 15400, len(dates))
noise = np.random.normal(0, 230, len(dates)).cumsum()
series = pd.DataFrame({"Date": dates, "Close": trend + noise})
series["Forecast"] = series["Close"].rolling(5, min_periods=1).mean().shift(1).bfill() + np.linspace(0,250,len(series))

left, right = st.columns([1.1,.9])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Added positioning:</b> This page frames the work as decomposition with ETS and forecasting with SARIMA/SARIMAX to show stronger applied forecasting skills.</p></div>', unsafe_allow_html=True)
    fig = px.line(series, x="Date", y=["Close", "Forecast"], template="plotly_dark", title="Nasdaq Close vs Forecast Illustration")
    fig.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.markdown("### Forecasting workflow")
    st.markdown('''<div class="section-box"><p style="color:#D1D5DB;line-height:1.7;">1. Load Nasdaq close series<br>2. Handle business-day frequency and interpolation<br>3. Difference the series<br>4. Diagnose autocorrelation using ACF and Ljung-Box<br>5. Test stationarity using ADF<br>6. Decompose with ETS<br>7. Forecast with SARIMA and SARIMAX</p></div>''', unsafe_allow_html=True)
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)
