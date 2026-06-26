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

show_header("yelp_header.png")


st.set_page_config(page_title="Customer Sentiment Intelligence", page_icon="💬", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='yelp')

#st.image(p['banner'], use_container_width=True)
st.title("Customer Sentiment Intelligence")
st.caption("Yelp Reviews · Binary Sentiment Analysis")
cols = st.columns(4)
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

left, right = st.columns([1.1,.9])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Business translation:</b> {p["business_value"]}</p></div>', unsafe_allow_html=True)
    df = pd.DataFrame({"Model":["Fine-tuned BERT", "Pre-trained DistilBERT"], "Accuracy":[0.957,0.869], "F1":[0.955,0.863]})
    fig = px.bar(df, x="Model", y=["Accuracy","F1"], barmode="group", template="plotly_dark", title="Sentiment Model Comparison")
    fig.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)
    review = st.text_area("Type a customer review", "The food was amazing and the staff were very friendly.")
    if st.button("Analyze sentiment"):
        neg_words = ["bad","cold","worst","terrible","rude","slow","disappointing"]
        sent = "Negative" if any(w in review.lower() for w in neg_words) else "Positive"
        st.success(f"Predicted sentiment: {sent}")
