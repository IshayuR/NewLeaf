import html as html_mod
import streamlit as st
from utils.document_data import DOCUMENTS
from utils.openai_client import call_gpt
from utils.ui import setup_page, render_hero, AI_DISCLOSURE_HTML

st.set_page_config(page_title="NewLeaf — Documents", page_icon="🍃", layout="centered")
setup_page()

render_hero("Get Your Documents", "Everything you need, step by step.", "📋")

st.markdown("""
<p style="font-size:0.95rem; color:#64748B; line-height:1.6;">
    Most jobs require a few key documents. Check off what you already have —
    we'll show you exactly how to get the rest.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

DOC_ICONS = {
    "State-issued Photo ID": "🪪",
    "Social Security Card": "🔢",
    "Birth Certificate": "📜",
    "Work Authorization (if applicable)": "🛂",
    "Bank Account or Prepaid Card": "💳",
}

for doc_name, info in DOCUMENTS.items():
    icon = DOC_ICONS.get(doc_name, "📄")
    checked = st.checkbox(f"I have my {doc_name}", key=f"doc_{doc_name}")

    if checked:
        st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #F0FDFA, #ECFDF5);
    border: 1px solid #A7F3D0;
    border-radius: 14px;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.7rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
">
    <span style="font-size:1.3rem;">✅</span>
    <span style="font-weight:600; color:#065F46; font-size:0.92rem;">{doc_name}</span>
</div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
<div style="
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #F59E0B;
    border-radius: 0 14px 14px 0;
    padding: 0.9rem 1.2rem;
    margin-bottom: 0.3rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
">
    <span style="font-size:1.3rem;">{icon}</span>
    <span style="font-weight:600; color:#92400E; font-size:0.92rem;">⚠️ {doc_name} — needed</span>
</div>
        """, unsafe_allow_html=True)

        with st.expander(f"How to get: {doc_name}"):
            st.markdown(f"**Why employers need it:** {info['why']}")
            st.markdown(f"**How to get it:** {info['how']}")
            st.markdown(f"**⏱️ Estimated time:** {info['time']}")

st.markdown("---")
st.markdown("#### 🔎 Find Local Help Near You")
st.markdown(
    '<p style="color:#64748B; font-size:0.92rem;">Enter your city and we\'ll find organizations that can help.</p>',
    unsafe_allow_html=True,
)

city = st.text_input(
    "What city are you in?",
    value=st.session_state.get("user_location", ""),
    placeholder="e.g., Hartford, CT",
)

RESOURCE_SYSTEM_PROMPT = (
    "List 3–5 real organizations in {city} that help people experiencing "
    "homelessness obtain IDs, birth certificates, or employment documents. "
    "For each, include the name, what they help with, and a website or "
    "phone number if known. If unsure about specific organizations, "
    "suggest practical ways to search locally."
)

if st.button("🍃 Find Local Help", use_container_width=True):
    if not city.strip():
        st.warning("Please enter a city name so we can search for you.")
    else:
        prompt = RESOURCE_SYSTEM_PROMPT.replace("{city}", city.strip())
        with st.spinner("🍃 Looking up resources in your area..."):
            try:
                results = call_gpt(
                    prompt,
                    f"Find organizations that help with documents in {city.strip()}.",
                )
                st.session_state["local_resources"] = results
            except Exception as e:
                st.error(f"Something went wrong: {e}")

if st.session_state.get("local_resources"):
    st.markdown("---")
    st.markdown("#### 📍 Resources We Found")

    safe_resources = html_mod.escape(st.session_state["local_resources"]).replace("\n", "<br>")

    st.markdown(f"""
<div style="
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #14B8A6;
    border-radius: 0 16px 16px 0;
    padding: 1.4rem 1.6rem;
    margin-top: 0.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    font-size: 0.92rem;
    line-height: 1.75;
    color: #334155;
">
    {safe_resources}
</div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div style="
    margin-top: 0.8rem;
    font-size: 0.8rem;
    color: #64748B;
    text-align: center;
">
    🍃 Always verify these resources are still active before visiting.
</div>
    """, unsafe_allow_html=True)

    st.markdown(AI_DISCLOSURE_HTML, unsafe_allow_html=True)
