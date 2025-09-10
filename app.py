import streamlit as st

st.set_page_config(
    page_title="AI Suite Demo Kit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define sections and modules
sections = {
    "Productivity Tools": [
        "AI@ Minutes",
        "AI@ AskPro",
        "AI@ Summary",
        "AI@ EmailWriter",
        "AI@ SmartReply"
    ],
    "Business Intelligence": ["AI@ DocReview", "AI@ SWOT"],
    "Data Management": ["AI@ NameCards", "AI@ MiniCRM", "AI@ Form", "AI@ Extract"],
    "Admin, HR & Finance": ["AI@ Recruitment", "AI@ ResumeScreen", "AI@ HRHandbook", "AI@ OfferLetter"],
    "Content & Marketing": ["AI@ CopyWriting", "AI@ Storyline"]
}

# Sidebar menu
st.sidebar.title("AI@ Suite Sections & Modules")
section = st.sidebar.selectbox("Select Section", list(sections.keys()))
module = st.sidebar.radio("Choose a module", sections[section])

# Main content
st.title("AI Suite Demo Kit")
st.markdown(f"### {module}", unsafe_allow_html=True)

module_name = module.split('@ ')[1] if "@ " in module else module
st.write(f"[The module {module_name}] demo kit")

# ------------------------
# Module-specific content
# ------------------------
if module == "AI@ AskPro":
    st.subheader("Use Case: Test HR chatbot")
    st.write("Type in the chatbox:")

    # Example Q1
    q1 = "I wanna knw the leave i can apply for"
    st.text(q1)
    st.markdown(
        f"""<button onclick="navigator.clipboard.writeText('{q1}')">📋 Copy</button>""",
        unsafe_allow_html=True
    )

    # Example Q2
    q2 = "who is the boss of WAC?"
    st.text(q2)
    st.markdown(
        f"""<button onclick="navigator.clipboard.writeText('{q2}')">📋 Copy</button>""",
        unsafe_allow_html=True
    )

elif module == "AI@ SWOT":
    st.subheader("Example: Crisis Management (PR & Reputation Risk)")

    st.markdown("**Situation**")
    st.write("Company faces a sudden data breach incident. Management needs a quick, structured view to plan their response.")

    st.markdown("**Strengths**")
    st.write("Established customer trust, strong IT recovery team.")

    st.markdown("**Weaknesses**")
    st.write("Lack of proactive communication plan, outdated security policy.")

elif module == "AI@ Summary":
    st.subheader("Paste Content")
    st.write("Workshop Learning Outcomes")

    st.markdown(
        """
        • Design and implement compelling adult learning experiences.  
        • Conduct thorough Training Needs Analyses (TNA) to identify learning priorities.  
        • Develop competency-based training (CBT) programs aligned with organizational goals.  
        • Deliver dynamic and impactful training sessions that engage learners.  
        • Facilitate active participation and promote meaningful learning interactions.  
        • Use strategic questioning techniques to ensure effective knowledge transfer.  
        • Address and manage challenging learner behaviours with confidence and professionalism.  
        • Incorporate technology and learning aids to enhance training delivery.  
        • Conduct competency-based assessments to evaluate learning outcomes accurately.  
        • Provide clear, actionable feedback to support participants' continuous improvement.  
        """
    )

    user_input = st.text_area("✍️ Paste your own content here for summary", height=200)

elif module == "AI@ EmailWriter":
    st.subheader("Example 1: Crisis / Error Handling (Support / Ops)")
    st.markdown("**Scenario:**")
    st.write(
        "Ops team needs to inform clients about a temporary system downtime.\n\n"
        "Team inputs the situation → AI drafts a message that is transparent, calm, "
        "and instructive, saving time under stress."
    )

    st.subheader("Example 2: Partnership Proposal (Business Development)")
    st.markdown("**Scenario:**")
    st.write(
        "A BD executive wants to propose a collaboration with another company.\n\n"
        "Provides key value points → AI generates a professional, persuasive proposal email "
        "that highlights mutual benefits."
    )
