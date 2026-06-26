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

show_header("drone_header.png")

# ============================================================

st.set_page_config(page_title="Drone Detection", page_icon="🛸", layout="wide")
apply_style(); sidebar()
p = next(x for x in PROJECTS if x['slug']=='drone')

#st.image(p['banner'], use_container_width=True)
st.title("Drone Detection in Airport Environments")
st.caption("Computer Vision · Object Detection · YOLO vs Faster R-CNN")
cols = st.columns(5)
for col, (label, value) in zip(cols, p['metrics']):
    col.markdown(f'<div class="metric-box"><div class="metric-label">{label}</div><div class="metric-value">{value}</div></div>', unsafe_allow_html=True)

left, right = st.columns([1.1,.9])
with left:
    st.markdown(f'<div class="section-box"><h2>Project objective</h2><p style="color:#D1D5DB;line-height:1.65;">{p["summary"]}</p><p style="color:#D1D5DB;line-height:1.65;"><b>Business translation:</b> {p["business_value"]}</p></div>', unsafe_allow_html=True)
    metrics = pd.DataFrame({"Metric":["Precision", "Recall", "mAP50", "mAP50-95"], "Baseline YOLO":[0.994,1.0,0.995,0.785], "Augmented YOLO":[0.995,1.0,0.995,0.579]})
    fig = px.bar(metrics, x="Metric", y=["Baseline YOLO", "Augmented YOLO"], barmode="group", template="plotly_dark", title="YOLO Detection Performance")
    fig.update_layout(paper_bgcolor="#050508", plot_bgcolor="#050508", font_color="white", yaxis_range=[0,1.1])
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.markdown("### Model comparison")
    st.markdown('''<div class="section-box"><p style="color:#D1D5DB;line-height:1.65;">YOLO delivered faster real-time performance, while Faster R-CNN showed stronger localization precision for small-object detection. This gives the project a strong practical trade-off: speed vs. localization quality.</p></div>''', unsafe_allow_html=True)
    st.markdown("### Skills demonstrated")
    st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in p['skills']]), unsafe_allow_html=True)
