import streamlit as st
import pandas as pd
from utils.ui import setup_page, render_hero

st.set_page_config(page_title="NewLeaf — Caseworker", page_icon="🍃", layout="centered")
setup_page()

if "caseworker_auth" not in st.session_state:
    st.session_state["caseworker_auth"] = False

if not st.session_state["caseworker_auth"]:
    render_hero("Caseworker Dashboard", "Track and support your clients.", "👥")

    st.markdown("""
<div style="
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 2rem 1.5rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    margin-bottom: 1rem;
">
    <div style="font-size: 2rem; margin-bottom: 0.6rem;">🔐</div>
    <p style="font-size: 0.95rem; color: #64748B; margin: 0;">
        This page is for caseworkers and program staff.
    </p>
</div>
    """, unsafe_allow_html=True)

    password = st.text_input("Enter access code:", type="password")
    if st.button("Log In", use_container_width=True):
        if password == "caseworker2026":
            st.session_state["caseworker_auth"] = True
            st.rerun()
        else:
            st.error("Incorrect code. Please try again.")
    st.stop()

render_hero("Caseworker Dashboard", "Track and support your clients.", "👥")

st.markdown("""
<p style="font-size:0.95rem; color:#64748B; line-height:1.6;">
    NewLeaf helps your clients take their next step — track their progress here.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

metrics = [
    ("Total Clients", "3", "👥", "#14B8A6", "#10B981"),
    ("Resumes Generated", "2", "📄", "#38BDF8", "#818CF8"),
    ("Jobs Viewed", "7", "💼", "#F59E0B", "#EF4444"),
]

cols = st.columns(3)
for col, (label, value, icon, c1, c2) in zip(cols, metrics):
    with col:
        st.markdown(f"""
<div style="
    background: white;
    border-radius: 16px;
    padding: 1.2rem 1rem;
    text-align: center;
    border: 1px solid #E2E8F0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
">
    <div style="
        width: 40px; height: 40px;
        background: linear-gradient(135deg, {c1}, {c2});
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem;
        margin: 0 auto 0.6rem auto;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
    ">{icon}</div>
    <div style="font-size: 2rem; font-weight: 800; color: #0F172A; letter-spacing: -0.03em;">{value}</div>
    <div style="font-size: 0.78rem; color: #64748B; font-weight: 500; margin-top: 0.15rem;">{label}</div>
</div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("#### 📋 Client Progress")

if "client_data" not in st.session_state:
    st.session_state["client_data"] = pd.DataFrame(
        {
            "Name": ["Maria S.", "James T.", "Aisha R."],
            "Last Active": ["Feb 27, 2026", "Feb 25, 2026", "Feb 26, 2026"],
            "Resume": ["✅ Complete", "✅ Complete", "⏳ In Progress"],
            "Jobs Viewed": [4, 2, 1],
            "Notes": [
                "Has interview Thursday — follow up",
                "Needs help getting State ID",
                "Just started — check back soon",
            ],
        }
    )

edited_df = st.data_editor(
    st.session_state["client_data"],
    use_container_width=True,
    num_rows="dynamic",
    key="client_editor",
)
st.session_state["client_data"] = edited_df

st.markdown("---")

if st.button("➕ Add New Client → Go to Onboarding", use_container_width=True):
    st.switch_page("pages/1_Onboarding.py")
