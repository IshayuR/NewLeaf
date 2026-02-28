import html as html_mod
import random
import streamlit as st
from utils.openai_client import call_gpt
from utils.resume_builder import build_resume_prompt, RESUME_SYSTEM_PROMPT
from utils.ui import setup_page, render_hero, AI_DISCLOSURE_HTML

st.set_page_config(page_title="NewLeaf — Build Your Resume", page_icon="🍃", layout="centered")
setup_page()

render_hero("Build Your Resume", "Let's tell your story.", "📄")

st.markdown("#### 👤 About you")
st.caption("Just a few quick questions — we'll handle the rest.")

with st.form("resume_form"):
    col_name, col_loc = st.columns(2)
    with col_name:
        name = st.text_input("First name", placeholder="e.g., Maria")
    with col_loc:
        location = st.text_input("City or ZIP code", placeholder="e.g., Hartford or 06103")

    st.markdown("")
    st.markdown("#### 💼 Experience & skills")

    experience = st.text_area(
        "What kind of work have you done before? Even odd jobs count.",
        placeholder="e.g., moved furniture, fast food, cleaned offices...",
        height=110,
    )
    skills = st.text_area(
        "What are you good at?",
        placeholder="e.g., cooking, driving, cleaning, talking to people...",
        height=90,
    )
    st.caption("No skill is too small — list anything you're comfortable doing.")

    st.markdown("")
    st.markdown("#### ⚙️ Availability")

    col_phys, col_avail = st.columns(2)
    with col_phys:
        physical_ability = st.selectbox(
            "Physically demanding work?",
            options=["Yes", "Somewhat", "No"],
        )
    with col_avail:
        availability = st.multiselect(
            "When can you work?",
            options=["Mornings", "Afternoons", "Evenings", "Weekends"],
            default=["Mornings", "Afternoons"],
        )

    has_gap = st.checkbox("I have a gap in my work history I'd like help explaining")

    submitted = st.form_submit_button("✨ Build My Resume", use_container_width=True)

if submitted:
    if not name.strip():
        st.warning("Please enter your first name so we can build your resume.")
    elif not experience.strip() and not skills.strip():
        st.warning("Please share at least some work experience or skills.")
    else:
        st.session_state["user_name"] = name.strip()
        st.session_state["user_location"] = location.strip()
        st.session_state["user_skills"] = skills.strip()
        st.session_state["user_experience"] = experience.strip()
        st.session_state["user_availability"] = availability

        user_message = build_resume_prompt(
            name=name.strip(),
            location=location.strip(),
            experience=experience.strip(),
            skills=skills.strip(),
            physical_ability=physical_ability,
            availability=availability,
            has_gap=has_gap,
        )

        with st.spinner("🍃 NewLeaf is building your resume..."):
            try:
                resume_text = call_gpt(RESUME_SYSTEM_PROMPT, user_message)
                st.session_state["resume"] = resume_text
                st.balloons()
            except Exception as e:
                st.error(f"Something went wrong generating your resume: {e}")
                st.stop()

if st.session_state.get("resume"):
    st.markdown("---")
    st.markdown("#### 📄 Your Resume")

    resume_text = st.session_state["resume"]
    safe_resume = html_mod.escape(resume_text)
    st.markdown(f"""
<div style="
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 1.8rem;
    font-family: 'Courier New', 'Courier', monospace;
    font-size: 0.85rem;
    line-height: 1.75;
    color: #1E293B;
    white-space: pre-wrap;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04), 0 1px 2px rgba(0,0,0,0.06);
">{safe_resume}</div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.download_button(
        label="⬇️ Download Resume",
        data=resume_text,
        file_name="NewLeaf_Resume.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.markdown(AI_DISCLOSURE_HTML, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📧 Your Temporary Email")

    if "temp_email" not in st.session_state:
        first = st.session_state.get("user_name", "user").lower().replace(" ", "")
        digits = random.randint(1000, 9999)
        st.session_state["temp_email"] = f"{first}_{digits}@newleafmail.info"

    st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #F0FDFA 0%, #ECFDF5 100%);
    border: 1px solid #A7F3D0;
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    text-align: center;
">
    <div style="font-size: 0.78rem; font-weight: 600; color: #065F46; text-transform: uppercase; letter-spacing: 0.06em; margin-bottom: 0.4rem;">
        Your Contact Email
    </div>
    <div style="font-size: 1.15rem; font-weight: 700; color: #047857; letter-spacing: 0.02em;">
        {st.session_state["temp_email"]}
    </div>
</div>
    """, unsafe_allow_html=True)

    st.markdown("")
    st.info(
        "Use this email on job applications. When you're ready, set up a "
        "free permanent email at **gmail.com** using a library or shelter computer."
    )
