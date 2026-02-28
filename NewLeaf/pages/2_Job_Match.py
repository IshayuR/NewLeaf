import html as html_mod
import streamlit as st
from utils.job_api import fetch_jobs
from utils.ui import setup_page, render_hero

st.set_page_config(page_title="NewLeaf — Find Jobs", page_icon="🍃", layout="centered")
setup_page()

render_hero("Find Jobs Near You", "Opportunities matched to your skills.", "💼")

col1, col2 = st.columns(2)
with col1:
    zip_code = st.text_input(
        "Your ZIP code or city",
        value=st.session_state.get("user_location", ""),
        placeholder="e.g., 06103",
    )
with col2:
    skills = st.text_input(
        "Skills or job type",
        value=st.session_state.get("user_skills", ""),
        placeholder="e.g., cleaning, cooking, warehouse",
    )

if st.button("🔍 Search Jobs", use_container_width=True):
    if not zip_code.strip():
        st.warning("Please enter a ZIP code or city name.")
    else:
        with st.spinner("Searching for jobs near you..."):
            jobs = fetch_jobs(zip_code.strip(), skills.strip())
            st.session_state["found_jobs"] = jobs

if st.session_state.get("found_jobs"):
    jobs = st.session_state["found_jobs"]

    st.markdown(f"""
<div style="
    display: inline-block;
    background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
    color: #065F46;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 1rem;
">
    ✅ Found {len(jobs)} job{"s" if len(jobs) != 1 else ""} for you
</div>
    """, unsafe_allow_html=True)

    for job in jobs:
        title = html_mod.escape(job.get("title", "Job Opening"))
        company = html_mod.escape(job.get("company", "Company"))
        location = html_mod.escape(job.get("location", ""))
        description = html_mod.escape(job.get("description", "")[:200])
        url = job.get("url", "#")
        salary = job.get("salary")

        salary_html = ""
        if salary:
            salary_html = f'<span style="display:inline-block; background:linear-gradient(135deg,#FFFBEB,#FEF3C7); color:#92400E; border-radius:20px; padding:0.2rem 0.7rem; font-size:0.75rem; font-weight:600; margin-left:0.4rem;">💰 {salary}</span>'

        st.markdown(f"""
<div style="
    background: white;
    border-radius: 16px;
    padding: 1.3rem 1.5rem;
    margin-bottom: 0.85rem;
    border: 1px solid #E2E8F0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);
    transition: all 0.25s ease;
">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:0.5rem;">
        <div style="flex:1; min-width:200px;">
            <h3 style="margin:0 0 0.25rem 0; font-size:1.05rem; font-weight:700; color:#0F172A !important;">{title}</h3>
            <p style="margin:0; color:#64748B; font-size:0.85rem;">🏢 {company} &nbsp;·&nbsp; 📍 {location}</p>
        </div>
        <span style="
            display:inline-block;
            background: linear-gradient(135deg, #ECFDF5, #D1FAE5);
            color: #065F46;
            border-radius: 20px;
            padding: 0.2rem 0.7rem;
            font-size: 0.72rem;
            font-weight: 600;
        ">Entry Level</span>
    </div>
    <p style="margin:0.7rem 0 0.8rem 0; font-size:0.9rem; color:#475569; line-height:1.55;">{description}...</p>
    <div style="display:flex; align-items:center; flex-wrap:wrap; gap:0.4rem;">
        <a href="{url}" target="_blank" style="
            display:inline-block;
            background: linear-gradient(135deg, #14B8A6, #10B981);
            color: white !important;
            padding: 0.4rem 1.1rem;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.85rem;
            box-shadow: 0 2px 6px rgba(20,184,166,0.2);
            transition: all 0.2s ease;
        ">View Job →</a>
        {salary_html}
    </div>
</div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("#### 🚀 Other Ways to Find Work Today")
st.markdown(
    '<p style="color:#64748B; font-size:0.92rem;">These options can get you working fast — no waiting.</p>',
    unsafe_allow_html=True,
)

resources = [
    ("💪", "Labor Ready / PeopleReady", "Walk in early, get assigned a job for the day, get paid at the end of the shift. No appointment needed.", "#14B8A6", "#10B981"),
    ("🏭", "Staffmark", "Temp agency with entry-level warehouse, cleaning, and factory jobs. Walk in and sign up.", "#38BDF8", "#14B8A6"),
    ("⚡", "Instawork", "Free app for same-day gig shifts (food service, warehouses, events). Download at a library.", "#6366F1", "#8B5CF6"),
    ("📱", "Wonolo", "App-based platform for daily and weekly gigs. You pick the shifts that work for you.", "#F59E0B", "#EF4444"),
    ("🔧", "TaskRabbit", "Get paid for moving, cleaning, or assembling furniture. Set your own schedule and rates.", "#EC4899", "#F43F5E"),
    ("🏢", "Local Day Labor Centers", "Free centers where you show up in the morning and get matched with work. Call 211.", "#34D399", "#14B8A6"),
]

for emoji, rname, desc, c1, c2 in resources:
    st.markdown(f"""
<div style="
    background: white;
    border-radius: 16px;
    padding: 1.1rem 1.3rem;
    margin-bottom: 0.7rem;
    border: 1px solid #E2E8F0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex;
    align-items: flex-start;
    gap: 0.9rem;
">
    <div style="
        width: 38px; height: 38px; min-width: 38px;
        background: linear-gradient(135deg, {c1}, {c2});
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.15rem;
    ">{emoji}</div>
    <div>
        <h3 style="margin:0 0 0.2rem 0; font-size:0.95rem; font-weight:700; color:#0F172A !important;">{rname}</h3>
        <p style="margin:0; font-size:0.85rem; color:#64748B; line-height:1.5;">{desc}</p>
    </div>
</div>
    """, unsafe_allow_html=True)
