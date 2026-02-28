import html as html_mod
import streamlit as st
from utils.openai_client import call_gpt
from utils.ui import setup_page, render_hero, AI_DISCLOSURE_HTML

st.set_page_config(page_title="NewLeaf — Interview Prep", page_icon="🍃", layout="centered")
setup_page()

render_hero("Practice Your Interview", "Confidence through preparation.", "🎤")

st.markdown("""
<p style="font-size:0.95rem; color:#64748B; line-height:1.6;">
    Interviews can feel scary — but practice makes them easier.
    Pick a question, write your answer, and get friendly AI feedback.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

QUESTIONS = [
    "Tell me about yourself.",
    "Why do you want this job?",
    "What are your strengths?",
    "Have you ever had a conflict with a coworker? How did you handle it?",
    "Why do you have a gap in your employment?",
    "Are you reliable? Can you give an example?",
    "What hours are you available?",
    "Do you have any questions for us?",
]

COACH_SYSTEM_PROMPT = (
    "You are a kind, encouraging interview coach helping someone who has "
    "experienced homelessness prepare for a job interview.\n"
    "Review their answer to the interview question. Give feedback in exactly "
    "3 short bullet points:\n"
    "1. What they did well\n"
    "2. One thing to improve or add\n"
    "3. A suggested improved version of their answer (max 3 sentences)\n"
    "Keep your tone warm, non-judgmental, and practical. "
    "Never make the person feel bad."
)

if "interview_feedback" not in st.session_state:
    st.session_state["interview_feedback"] = None
if "interview_question" not in st.session_state:
    st.session_state["interview_question"] = QUESTIONS[0]

selected = st.selectbox(
    "Pick an interview question to practice:",
    options=QUESTIONS,
    index=QUESTIONS.index(st.session_state["interview_question"]),
    key="question_select",
)
st.session_state["interview_question"] = selected

st.markdown(f"""
<div style="
    background: linear-gradient(135deg, #F0FDFA 0%, #ECFDF5 100%);
    border: 1px solid #A7F3D0;
    border-radius: 14px;
    padding: 1.1rem 1.4rem;
    margin: 0.8rem 0 1rem 0;
">
    <div style="font-size:0.72rem; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; color:#065F46; margin-bottom:0.35rem;">
        Interview Question
    </div>
    <div style="font-size:1.05rem; font-weight:500; color:#0F172A; line-height:1.4;">
        &ldquo;{selected}&rdquo;
    </div>
</div>
""", unsafe_allow_html=True)

answer = st.text_area(
    "Write your answer here — don't worry about being perfect.",
    height=150,
    placeholder="Just write how you'd actually say it...",
    key="interview_answer",
)

if st.button("✨ Get Feedback", use_container_width=True):
    if not answer.strip():
        st.warning("Write something first — even a short answer is fine!")
    else:
        user_msg = (
            f"Interview question: \"{selected}\"\n\n"
            f"The person's answer: \"{answer.strip()}\""
        )
        with st.spinner("🍃 Thinking about your answer..."):
            try:
                feedback = call_gpt(COACH_SYSTEM_PROMPT, user_msg)
                st.session_state["interview_feedback"] = feedback
            except Exception as e:
                st.error(f"Something went wrong: {e}")

if st.session_state["interview_feedback"]:
    st.markdown("---")

    safe_feedback = html_mod.escape(st.session_state["interview_feedback"]).replace("\n", "<br>")

    st.markdown(f"""
<div style="
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-left: 4px solid #14B8A6;
    border-radius: 0 16px 16px 0;
    padding: 1.4rem 1.6rem;
    margin-top: 0.5rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
">
    <div style="
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.8rem;
    ">
        <div style="
            width: 32px; height: 32px;
            background: linear-gradient(135deg, #14B8A6, #10B981);
            border-radius: 8px;
            display: flex; align-items: center; justify-content: center;
            font-size: 0.9rem;
        ">🍃</div>
        <span style="font-weight: 700; font-size: 0.95rem; color: #0F172A;">NewLeaf Feedback</span>
    </div>
    <div style="font-size: 0.92rem; line-height: 1.75; color: #334155;">
        {safe_feedback}
    </div>
</div>
    """, unsafe_allow_html=True)

    st.markdown(AI_DISCLOSURE_HTML, unsafe_allow_html=True)

    st.markdown("")
    if st.button("🔄 Try Another Question"):
        st.session_state["interview_feedback"] = None
        current_idx = QUESTIONS.index(st.session_state["interview_question"])
        next_idx = (current_idx + 1) % len(QUESTIONS)
        st.session_state["interview_question"] = QUESTIONS[next_idx]
        st.rerun()
