import streamlit as st

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --nl-bg: #F8FAFB;
    --nl-card: #FFFFFF;
    --nl-text: #0F172A;
    --nl-muted: #64748B;
    --nl-border: #E2E8F0;
    --nl-accent-1: #14B8A6;
    --nl-accent-2: #10B981;
    --nl-accent-3: #34D399;
    --nl-gradient: linear-gradient(135deg, #14B8A6 0%, #10B981 50%, #34D399 100%);
    --nl-gradient-warm: linear-gradient(135deg, #10B981 0%, #34D399 40%, #6EE7B7 100%);
    --nl-gradient-vibrant: linear-gradient(135deg, #14B8A6 0%, #38BDF8 50%, #818CF8 100%);
    --nl-shadow-sm: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);
    --nl-shadow-md: 0 4px 12px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.04);
    --nl-shadow-lg: 0 10px 30px rgba(0,0,0,0.08), 0 4px 8px rgba(0,0,0,0.04);
    --nl-radius: 16px;
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--nl-bg) !important;
    color: var(--nl-text);
    -webkit-font-smoothing: antialiased;
}

.block-container {
    padding-top: 4rem;
    padding-bottom: 3rem;
    max-width: 740px;
}

/* ── Typography ── */
h1 {
    font-size: 1.9rem;
    font-weight: 800;
    color: var(--nl-text) !important;
    letter-spacing: -0.03em;
}
h2 {
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--nl-text) !important;
    letter-spacing: -0.02em;
}
h3 {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--nl-text) !important;
}
p, li, span, label, div {
    color: var(--nl-text);
}

/* ── Buttons ── */
div.stButton > button,
div.stFormSubmitButton > button {
    background: var(--nl-gradient) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px;
    padding: 0.65rem 1.6rem;
    font-size: 0.95rem;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.01em;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 8px rgba(20,184,166,0.25);
    width: 100%;
}
div.stButton > button:hover,
div.stFormSubmitButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(20,184,166,0.35) !important;
    color: white !important;
}
div.stButton > button:active,
div.stFormSubmitButton > button:active {
    transform: translateY(0);
}

div.stDownloadButton > button {
    background: var(--nl-gradient) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px;
    padding: 0.65rem 1.6rem;
    font-size: 0.95rem;
    font-weight: 600;
    font-family: 'Inter', sans-serif;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 8px rgba(20,184,166,0.25);
    width: 100%;
}
div.stDownloadButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(20,184,166,0.35) !important;
    color: white !important;
}

/* ── Inputs ── */
input, textarea, select {
    border-radius: 12px !important;
    border: 1.5px solid var(--nl-border) !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 0.8rem !important;
    color: var(--nl-text) !important;
    background-color: var(--nl-card) !important;
    transition: all 0.2s ease;
}
input:focus, textarea:focus {
    border-color: var(--nl-accent-1) !important;
    box-shadow: 0 0 0 3px rgba(20,184,166,0.12) !important;
}

/* Hide search box inside selectbox dropdowns (keep functional) */
div[data-baseweb="select"] input {
    height: 0 !important;
    padding: 0 !important;
    border: none !important;
    min-height: 0 !important;
    overflow: hidden !important;
    caret-color: transparent !important;
}
div[data-baseweb="popover"] input {
    height: 0 !important;
    padding: 0 !important;
    border: none !important;
    min-height: 0 !important;
    overflow: hidden !important;
    caret-color: transparent !important;
}

/* ── Cards ── */
.nl-card {
    background: var(--nl-card);
    border-radius: var(--nl-radius);
    padding: 1.3rem 1.5rem;
    margin-bottom: 0.85rem;
    border: 1px solid var(--nl-border);
    box-shadow: var(--nl-shadow-sm);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.nl-card:hover {
    box-shadow: var(--nl-shadow-md);
    border-color: #CBD5E1;
    transform: translateY(-1px);
}

.nl-card-gradient {
    background: var(--nl-card);
    border-radius: var(--nl-radius);
    padding: 1.3rem 1.5rem;
    margin-bottom: 0.85rem;
    border: 1px solid transparent;
    background-clip: padding-box;
    box-shadow: var(--nl-shadow-sm);
    position: relative;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.nl-card-gradient::before {
    content: '';
    position: absolute;
    inset: -1px;
    border-radius: var(--nl-radius);
    padding: 1.5px;
    background: var(--nl-gradient);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    pointer-events: none;
}
.nl-card-gradient:hover {
    box-shadow: var(--nl-shadow-lg);
    transform: translateY(-2px);
}

/* ── Tags ── */
.nl-tag {
    display: inline-block;
    background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
    color: #065F46;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}
.nl-tag-blue {
    background: linear-gradient(135deg, #EFF6FF, #DBEAFE);
    color: #1E40AF;
}
.nl-tag-amber {
    background: linear-gradient(135deg, #FFFBEB, #FEF3C7);
    color: #92400E;
}

/* ── Alerts ── */
.stAlert {
    border-radius: 14px !important;
    font-size: 0.92rem !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #047857 0%, #059669 40%, #10B981 100%) !important;
}
[data-testid="stSidebar"] * {
    color: #ECFDF5 !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] b,
[data-testid="stSidebar"] strong {
    color: #FFFFFF !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNavLink"] {
    border-radius: 10px;
    margin: 2px 8px;
    padding: 0.5rem 0.8rem;
    transition: background 0.2s ease;
}
[data-testid="stSidebar"] [data-testid="stSidebarNavLink"]:hover {
    background: rgba(255,255,255,0.1);
}
[data-testid="stSidebar"] [data-testid="stSidebarNavLink"][aria-current="page"] {
    background: rgba(255,255,255,0.15);
}

/* ── Dividers ── */
hr {
    border: none;
    border-top: 1px solid var(--nl-border);
    margin: 1.5rem 0;
}

/* ── Expanders ── */
div[data-testid="stExpander"] {
    border: 1px solid var(--nl-border);
    border-radius: 14px;
    overflow: hidden;
}
div[data-testid="stExpander"] summary {
    font-weight: 500;
}

/* ── Data editor / tables ── */
[data-testid="stDataEditor"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid var(--nl-border);
}

/* ── Hide only the hamburger menu, footer, and heading anchors ── */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stMarkdown a[href^="#"],
h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
    display: none !important;
}
</style>
"""

AI_DISCLOSURE_HTML = """
<div style="
    margin-top: 2rem;
    padding: 0.75rem 1.2rem;
    background: linear-gradient(135deg, #F0FDFA 0%, #ECFDF5 100%);
    border: 1px solid #A7F3D0;
    border-radius: 12px;
    font-size: 0.78rem;
    color: #065F46;
    text-align: center;
    letter-spacing: 0.01em;
">
    ✨ <b>AI Disclosure:</b> Generated by GPT-4o (OpenAI).
    NewLeaf uses AI to assist — always review before submitting to employers.
</div>
"""


def inject_css():
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("""
<div style="padding: 0.5rem 0 1rem 0; text-align:center;">
    <div style="display:inline-flex; align-items:center; gap:0.5rem; justify-content:center;">
        <span style="font-size: 1.6rem;">🍃</span>
        <span style="font-size: 1.35rem; font-weight: 800; color: white !important; letter-spacing: -0.02em;">NewLeaf</span>
    </div>
    <div style="font-size: 0.8rem; color: #A7F3D0 !important; margin-top: 0.3rem;">A fresh start, one step at a time.</div>
</div>
        """, unsafe_allow_html=True)
        st.markdown("""
<div style="
    font-size: 0.72rem;
    color: #6EE7B7 !important;
    text-align: center;
    padding: 0.5rem 0;
    opacity: 0.8;
">
    Built for HackUConn 2026<br>
    Theme: Living with AI 🤖
</div>
        """, unsafe_allow_html=True)


def render_hero(title, subtitle, emoji):
    st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #059669 0%, #10B981 40%, #14B8A6 100%);
    border-radius: 20px;
    padding: 2.5rem 2rem 2rem 2rem;
    margin-bottom: 1.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(16,185,129,0.2);
">
    <div style="
        position: absolute;
        top: -40px; right: -40px;
        width: 160px; height: 160px;
        background: radial-gradient(circle, rgba(110,231,183,0.2) 0%, transparent 70%);
        border-radius: 50%;
    "></div>
    <div style="
        position: absolute;
        bottom: -30px; left: -30px;
        width: 120px; height: 120px;
        background: radial-gradient(circle, rgba(56,189,248,0.15) 0%, transparent 70%);
        border-radius: 50%;
    "></div>
    <div style="font-size: 2.8rem; margin-bottom: 0.6rem; position:relative;">{emoji}</div>
    <div style="
        color: white;
        margin: 0;
        font-size: 1.85rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        position: relative;
    ">{title}</div>
    <div style="
        color: #A7F3D0;
        margin-top: 0.5rem;
        font-size: 1rem;
        font-weight: 400;
        position: relative;
    ">{subtitle}</div>
</div>
    """, unsafe_allow_html=True)


def setup_page():
    inject_css()
    render_sidebar()
