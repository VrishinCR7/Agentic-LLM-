import streamlit as st
from core.goal import Goal
from agents.controller import run_agent
from core.voice import generate_speech

st.set_page_config(
    page_title="Autonomous MVP Builder",
    layout="wide"
)

st.title("🚀 Autonomous MVP Builder")
st.markdown(
    """
    Turn high-level startup ideas into structured execution blueprints.
    """
)

with st.sidebar:
    st.header("⚙️ Configuration")
    iteration_limit = st.slider("Max Iterations", 1, 5, 3)
    st.markdown("---")
    st.markdown("Built on Execution-First Architecture")

voice_enabled = st.sidebar.toggle(
    "🔊 Voice Output",
    value=False
)


goal_input = st.text_area(
    "Describe your startup idea:",
    placeholder="Example: Build a B2B AI tool that automates contract review for startups..."
)

constraints_input = st.text_input(
    "Constraints (optional)",
    placeholder="Budget under $10k, launch in 30 days"
)

success_input = st.text_input(
    "Success Criteria (optional)",
    placeholder="Clear product scope, tech stack, go-to-market plan"
)

if st.button("⚡ Build My MVP Plan"):

    constraints = [c.strip() for c in constraints_input.split(",") if c.strip()]
    success_conditions = [s.strip() for s in success_input.split(",") if s.strip()]

    goal = Goal(
        outcome=goal_input,
        constraints=constraints,
        success_conditions=success_conditions
    )

    goal.max_iterations = iteration_limit

    with st.spinner("Autonomously planning, executing, and verifying..."):

        result = run_agent(goal)

    st.markdown("## 📊 Execution Status")
    st.success(result["status"])

    st.markdown("### 🔍 Progress Score")
    st.progress(result["progress"])

    st.markdown("## 🧠 Final Blueprint")
    st.write(result["output"])

    st.markdown("---")
    st.markdown("## 💰 Estimated Build Effort")

    if voice_enabled:

        with st.spinner("Generating voice output..."):

            audio_file = generate_speech(result["output"])

            if audio_file:
                st.audio(audio_file)

    estimated_cost = int(result["progress"] * 5000)
    st.write(f"Estimated development cost: ${estimated_cost}")