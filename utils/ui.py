import streamlit as st


def apply_style():
    st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: #050508; color: #fff; }
    section[data-testid="stSidebar"] { background: linear-gradient(180deg,#09090B,#111827); border-right:1px solid #27272a; }
    .block-container { padding-top: 2rem; max-width: 1400px; }
    h1 { font-size: 4.2rem !important; line-height: 1.0 !important; font-weight: 900 !important; letter-spacing: -2px; }
    h2 { font-weight: 850 !important; letter-spacing: -1px; }
    .hero {
        padding: 54px 48px; border-radius: 32px; margin-bottom: 34px;
        background: radial-gradient(circle at 20% 20%, rgba(239,68,68,.35), transparent 32%),
                    radial-gradient(circle at 80% 0%, rgba(59,130,246,.32), transparent 28%),
                    linear-gradient(135deg,#111827,#050508 70%);
        border: 1px solid rgba(255,255,255,.12);
        box-shadow: 0 30px 90px rgba(0,0,0,.45);
    }
    .hero-subtitle { color:#D1D5DB; font-size: 1.25rem; max-width: 840px; line-height:1.55; }
    .badge { display:inline-block; padding:7px 12px; border-radius:999px; background:rgba(239,68,68,.18); color:#FCA5A5; border:1px solid rgba(239,68,68,.35); font-weight:700; font-size:.85rem; margin-bottom:14px; }
    .netflix-row-title { font-size:1.55rem; font-weight:850; margin: 30px 0 16px 0; }
    .project-card {
        border-radius:24px; padding:0; overflow:hidden; background:#111827;
        border:1px solid rgba(255,255,255,.10); min-height:410px;
        transition: all .2s ease; box-shadow: 0 18px 50px rgba(0,0,0,.35);
    }
    .project-card:hover { transform: translateY(-5px); border-color:rgba(255,255,255,.28); }
    .project-body { padding: 22px; }
    .project-title { font-size:1.45rem; font-weight:850; line-height:1.15; margin: 8px 0; }
    .project-subtitle { color:#CBD5E1; font-size:.95rem; line-height:1.35; min-height:42px; }
    .tag { display:inline-block; padding:5px 10px; border-radius:999px; color:white; font-size:.75rem; font-weight:750; margin-right:6px; background:rgba(255,255,255,.12); }
    .metric-grid { display:grid; grid-template-columns: repeat(4,1fr); gap:16px; margin:24px 0; }
    .metric-box { background:#101827; border:1px solid rgba(255,255,255,.12); border-radius:20px; padding:18px; }
    .metric-label { color:#9CA3AF; font-size:.85rem; font-weight:700; }
    .metric-value { color:white; font-size:1.7rem; font-weight:900; margin-top:8px; }
    .section-box { background:#0B1220; border:1px solid rgba(255,255,255,.10); border-radius:26px; padding:26px; margin:22px 0; }
    .skill-pill { display:inline-block; padding:8px 12px; background:#151B2D; color:#E5E7EB; border:1px solid rgba(255,255,255,.10); border-radius:999px; margin:5px; font-weight:650; font-size:.88rem; }
    .footer { color:#6B7280; text-align:center; padding:40px 0 18px; font-size:.9rem; }
    div[data-testid="stButton"] > button {
        background: #E50914; color: white; border: 0; border-radius: 999px; padding: .65rem 1.15rem; font-weight: 800;
    }
    div[data-testid="stButton"] > button:hover { background:#F43F5E; color:white; border:0; }
    [data-testid="stMarkdownContainer"] a { color:#93C5FD; }
    .sidebar-brand { padding:18px; border-radius:22px; background:linear-gradient(135deg,#18181B,#111827); border:1px solid rgba(255,255,255,.12); margin-bottom:22px; }
    .sidebar-brand-title { font-size:1.1rem; font-weight:900; color:#fff; line-height:1.2; }
    .sidebar-brand-sub { color:#A1A1AA; font-size:.82rem; margin-top:8px; }
    </style>
    ''', unsafe_allow_html=True)


def sidebar():
    st.sidebar.markdown('''
    <div class="sidebar-brand">
      <div style="font-size:2.2rem;">🎬🤖</div>
      <div class="sidebar-brand-title">AI Research &<br>Applied ML Portfolio</div>
      <div class="sidebar-brand-sub">NLP · LLMs · Vision · Forecasting · Risk</div>
    </div>
    ''', unsafe_allow_html=True)
