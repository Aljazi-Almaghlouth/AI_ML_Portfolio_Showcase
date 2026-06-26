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

show_header("bbc_header.png")


st.set_page_config(page_title="Executive Text Summarization", page_icon="📄", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='summarization')

#st.image(p['banner'], use_container_width=True)
st.title("Executive Text Summarization")
st.caption("BBC News Summary Dataset · T5 Fine-Tuning")
cols = st.columns(len(p['metrics']))
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

left, right = st.columns([1,1])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Business translation:</b> {p["business_value"]}</p></div>', unsafe_allow_html=True)
    rouge_df = pd.DataFrame({"Model":["Fine-tuned T5", "Pre-trained T5"], "ROUGE-1 F1":[0.4197,0.3641], "ROUGE-L F1":[0.3945,0.2660]})
    fig = px.bar(rouge_df, x="Model", y=["ROUGE-1 F1","ROUGE-L F1"], barmode="group", template="plotly_dark", title="Fine-tuned vs Pre-trained T5")
    fig.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)
    article = st.text_area("Paste article text", "Federal regulators are preparing proposals to loosen capital requirements for banks after industry feedback.", height=170)
    if st.button("Generate executive summary"):
        st.info("Executive summary: Regulators are reviewing bank capital requirements, signaling potential policy changes that may affect financial institutions and market risk expectations.")
