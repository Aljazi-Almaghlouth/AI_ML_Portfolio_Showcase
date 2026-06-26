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

show_header("reuters_header.png")

# ============================================================
st.set_page_config(page_title="Financial News Classification", page_icon="📰", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='news')

#st.image(p['banner'], use_container_width=True)
st.title("Financial News Classification")
st.caption("Reuters Dataset · Multi-Class NLP Classification")

cols = st.columns(4)
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

left, right = st.columns([1.2, .8])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Business translation:</b> {p["business_value"]}</p></div>', unsafe_allow_html=True)
    topic_data = pd.DataFrame({
        "Topic": ["Class 3", "Class 4", "Class 19", "Class 16", "Class 1", "Other classes"],
        "Count": [3159, 1949, 549, 444, 432, 2449]
    })
    fig = px.bar(topic_data, x="Topic", y="Count", title="Illustrative Reuters Topic Distribution", color="Topic", template="plotly_dark")
    fig.update_layout(showlegend=False, paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.markdown('<div class="section-box"><h2>Model pipeline</h2><p style="color:#CBD5E1;line-height:1.7;">Raw newswire → word index sequence → 10K-vector representation → Dense layers → 46-way softmax probability distribution.</p></div>', unsafe_allow_html=True)
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)

st.markdown("### Mini demo")
text = st.text_area("Paste a sample financial news sentence", "Oil prices surge after production cuts and renewed market uncertainty.")
if st.button("Classify news topic"):
    topic = "Energy / Commodities" if any(k in text.lower() for k in ["oil","gas","energy","commodity"]) else "Corporate / Market News"
    st.success(f"Predicted topic: {topic}")
