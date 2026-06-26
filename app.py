import streamlit as st
from utils.ui import apply_style, sidebar
from data.projects import PROJECTS

import streamlit as st
from pathlib import Path

from data.projects import PROJECTS
from utils.ui import apply_style, sidebar


# ============================================================
# Page Config
# ============================================================

st.set_page_config(
    page_title="AI Research & Applied Machine Learning Portfolio",
    page_icon="🎬",
    layout="wide"
)

apply_style()
sidebar()


# ============================================================
# Paths
# ============================================================

assets_path = Path(__file__).resolve().parent / "assets"


# ============================================================
# Hero Section
# ============================================================

st.markdown("""
<div class="hero">
  <div class="badge">AI PORTFOLIO · NETFLIX STYLE SHOWCASE</div>
  <h1>AI Research &<br>Applied Machine Learning Portfolio</h1>
  <p class="hero-subtitle">
    A curated showcase of applied AI projects across NLP, large language models,
    computer vision, time-series forecasting, and financial risk analytics —
    built as product-style case studies rather than static notebooks.
  </p>
</div>
""", unsafe_allow_html=True)


# ============================================================
# Summary Metrics
# ============================================================

cols = st.columns(4)

summary_metrics = [
    ("AI Projects", "7"),
    ("NLP / LLM", "4"),
    ("Vision", "1"),
    ("Forecasting & Risk", "2")
]

for col, (label, val) in zip(cols, summary_metrics):
    col.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{val}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# Featured Projects
# ============================================================
# ============================================================
# Featured Projects
# ============================================================

st.markdown("## Featured Projects")

assets_path = Path(__file__).resolve().parent / "assets"

project_images = [
    "reuters_header.png",
    "bbc_header.png",
    "yelp_header.png",
    "imdb_header.png",
    "drone_header.png",
    "nasdaq_header.png",
    "risk_header.png",
]

for i in range(0, len(PROJECTS), 3):
    cols = st.columns(3)

    for j, (col, project) in enumerate(zip(cols, PROJECTS[i:i+3])):
        with col:
            image_file = project_images[i + j]
            image_path = assets_path / image_file

            if image_path.exists():
                st.image(str(image_path), use_container_width=True)
            else:
                st.error(f"Image not found: {image_file}")

            st.markdown(f"### {project.get('emoji', '')} {project['title']}")
            st.markdown(f"**{project['subtitle']}**")
            st.write(project.get("summary", project.get("description", "")))

            badges = project.get("badges", [])
            if badges:
                st.caption(" · ".join(badges[:4]))

            st.divider()

# ============================================================
# Portfolio Narrative
# ============================================================

st.markdown("""
<div class="section-box">
    <h2>Portfolio narrative</h2>
    <p style="color:#D1D5DB;font-size:1.05rem;line-height:1.65;">
        This portfolio positions Aljazi as a practical AI builder: able to work with
        text classification, summarization, sentiment modeling, parameter-efficient
        fine-tuning, object detection, market forecasting, and portfolio risk analytics.
        The focus is not only on model building, but also on translating models into
        decision-support products.
    </p>
</div>

<div class="footer">
    AI Research & Applied Machine Learning Portfolio · Prototype Version 1.0 · Developed by Aljazi Al Maghlouth
</div>
""", unsafe_allow_html=True)