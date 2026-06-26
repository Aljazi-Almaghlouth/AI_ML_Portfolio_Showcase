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

show_header("imdb_header.png")

# ============================================================
st.set_page_config(page_title="LoRA Sentiment Fine-Tuning", page_icon="🚀", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='lora')

#st.image(p['banner'], use_container_width=True)
st.title("LoRA Sentiment Fine-Tuning")
st.caption("IMDB Reviews · DistilBERT · Parameter-Efficient Fine-Tuning")
cols = st.columns(4)
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

comparison = pd.DataFrame({
    "Model": ["Full FT", "LoRA", "Adapter"],
    "Trainable parameters": [66955010, 739586, 100674],
    "Accuracy": [0.8988, 0.89424, 0.8408],
    "Precision": [0.897528, 0.880423, 0.835645],
    "Recall": [0.9004, 0.9124, 0.84848],
    "F1": [0.898962, 0.896126, 0.8420],
})
left, right = st.columns([1.05,.95])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Business translation:</b> {p["business_value"]}</p></div>', unsafe_allow_html=True)
    fig = px.bar(comparison, x="Model", y="F1", text="F1", template="plotly_dark", title="Performance Comparison")
    fig.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white", yaxis_range=[0.7, 1.0])
    st.plotly_chart(fig, use_container_width=True)
with right:
    fig2 = px.bar(comparison, x="Model", y="Trainable parameters", text="Trainable parameters", template="plotly_dark", title="Parameter Efficiency")
    fig2.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)

st.dataframe(comparison, use_container_width=True, hide_index=True)
