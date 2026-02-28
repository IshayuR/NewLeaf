import streamlit as st
from utils.ui import setup_page, render_hero

st.set_page_config(page_title="Home — NewLeaf", page_icon="🍃", layout="centered")
setup_page()

render_hero("Welcome to NewLeaf", "A fresh start, one step at a time.", "🍃")

st.markdown("""
<p style="text-align:center; font-size:1.05rem; color:#64748B; margin-bottom:1.5rem;">
    Free tools to help you build a resume, find work, and prepare for interviews.
    <br>Everything is <b style="color:#10B981;">private</b>, <b style="color:#10B981;">free</b>,
    and built with you in mind.
</p>
""", unsafe_allow_html=True)

features = [
    ("📝", "Build Your Resume", "Answer a few simple questions and get a professional resume — no experience needed.", "#14B8A6", "#10B981"),
    ("💼", "Find Jobs Near You", "Search entry-level jobs in your area, plus same-day work options.", "#38BDF8", "#14B8A6"),
    ("🎤", "Practice Interviews", "Try answering common questions and get friendly, helpful AI feedback.", "#6366F1", "#8B5CF6"),
    ("📋", "Get Your Documents", "Step-by-step guide to getting the paperwork you need for a job.", "#F59E0B", "#EF4444"),
]

col1, col2 = st.columns(2)
for i, (emoji, title, desc, c1, c2) in enumerate(features):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
<div style="
    background: white;
    border-radius: 18px;
    padding: 1.5rem;
    margin-bottom: 0.85rem;
    border: 1px solid #E2E8F0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    cursor: default;
">
    <div style="
        width: 44px; height: 44px;
        background: linear-gradient(135deg, {c1}, {c2});
        border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.4rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    ">{emoji}</div>
    <h3 style="margin:0 0 0.35rem 0; font-size:1.05rem; font-weight:700; color:#0F172A !important;">{title}</h3>
    <p style="margin:0; font-size:0.88rem; color:#64748B; line-height:1.5;">{desc}</p>
</div>
        """, unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align: center;
    padding: 1.5rem 1rem;
    margin-top: 0.5rem;
">
    <p style="font-size: 0.95rem; color: #64748B;">
        👉 <b style="color:#0F172A;">Tap the sidebar</b> (arrow at top-left on mobile) to get started.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align: center;
    padding: 0.6rem;
    margin-top: 0.5rem;
    font-size: 0.75rem;
    color: #94A3B8;
">
    NewLeaf — HackUConn 2026 &nbsp;·&nbsp; Theme: Living with AI 🤖
</div>
""", unsafe_allow_html=True)
