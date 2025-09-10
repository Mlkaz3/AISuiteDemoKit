import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AI Suite Demo Kit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------
# Reusable copy button
# -----------------------
def copy_button(text: str, key: str):
    """Renders a copy-to-clipboard button with JS"""
    components.html(
        f"""
        <div style="display:flex; align-items:center; margin-bottom:10px;">
            <button id="copy-btn-{key}" style="
                padding:6px 12px;
                border-radius:8px;
                border:1px solid #ccc;
                background:#f9f9f9;
                cursor:pointer;
                font-size:14px;
            ">📋 Copy</button>
        </div>
        <script>
        const btn = document.getElementById("copy-btn-{key}");
        btn.addEventListener("click", function() {{
            navigator.clipboard.writeText(`{text}`);
            btn.innerText = "✅ Copied!";
            setTimeout(() => btn.innerText = "📋 Copy", 1500);
        }});
        </script>
        """,
        height=45,
    )

# -----------------------
# Define sections & modules
# -----------------------
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

# -----------------------
# Sidebar navigation
# -----------------------
st.sidebar.title("AI@ Suite Sections & Modules")
section = st.sidebar.selectbox("Select Section", list(sections.keys()))
module = st.sidebar.radio("Choose a module", sections[section])

# -----------------------
# Main content
# -----------------------
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

    q1 = "I wanna knw the leave i can apply for"
    st.code(q1, language="text")
    copy_button(q1, key="askpro_q1")

    q2 = "who is the boss of WAC?"
    st.code(q2, language="text")
    copy_button(q2, key="askpro_q2")

elif module == "AI@ SWOT":
    st.subheader("Example: Crisis Management (PR & Reputation Risk)")

    situation = "Company faces a sudden data breach incident. Management needs a quick, structured view to plan their response."
    st.markdown("**Situation**")
    st.code(situation, language="text")
    copy_button(situation, key="swot_situation")

    strengths = "Established customer trust, strong IT recovery team."
    st.markdown("**Strengths**")
    st.code(strengths, language="text")
    copy_button(strengths, key="swot_strengths")

    weaknesses = "Lack of proactive communication plan, outdated security policy."
    st.markdown("**Weaknesses**")
    st.code(weaknesses, language="text")
    copy_button(weaknesses, key="swot_weaknesses")

elif module == "AI@ Summary":
    st.subheader("Paste Content")
    summary_text = """Workshop Learning Outcomes
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
    st.code(summary_text, language="text")
    copy_button(summary_text, key="summary_demo")

    user_input = st.text_area("✍️ Paste your own content here for summary", height=200)

elif module == "AI@ EmailWriter":
    st.subheader("Example 1: Crisis / Error Handling (Support / Ops)")
    example1 = """Scenario:
Ops team needs to inform clients about a temporary system downtime.
Team inputs the situation → AI drafts a message that is transparent, calm, and instructive, saving time under stress."""
    st.code(example1, language="text")
    copy_button(example1, key="emailwriter_ex1")

    st.subheader("Example 2: Partnership Proposal (Business Development)")
    example2 = """Scenario:
A BD executive wants to propose a collaboration with another company.
Provides key value points → AI generates a professional, persuasive proposal email that highlights mutual benefits."""
    st.code(example2, language="text")
    copy_button(example2, key="emailwriter_ex2")
