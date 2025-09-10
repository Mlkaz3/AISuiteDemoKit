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

# module_name = module.split('@ ')[1] if "@ " in module else module
# st.write(f"[The module {module_name}] demo kit")

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

elif module == "AI@ Minutes":
    # Raw GitHub URL of the image
    img_url = "https://raw.githubusercontent.com/Mlkaz3/AISuiteDemoKit/main/source/AIminutespic/1.png"

    # Display the image
    st.image(img_url, caption="AI Minutes Screenshot", use_container_width=True)

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
    st.write("Copy the paste content")
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

    # user_input = st.text_area("✍️ Paste your own content here for summary", height=200)

elif module == "AI@ EmailWriter":
    st.subheader("Example 1: Crisis / Error Handling (Support / Ops)")
    st.write("Scenario:")
    example1 = """
Ops team needs to inform clients about a temporary system downtime.
"""
    st.code(example1, language="text")
    st.write("Team inputs the situation → AI drafts a message that is transparent, calm, and instructive, saving time under stress.")
    copy_button(example1, key="emailwriter_ex1")

    st.subheader("Example 2: Partnership Proposal (Business Development)")
    st.write("Scenario:")
    example2 = """
A BD executive wants to propose a collaboration with another company.
"""
    st.code(example2, language="text")
    st.write("Provides key value points → AI generates a professional, persuasive proposal email that highlights mutual benefits.")
    copy_button(example2, key="emailwriter_ex2")

elif module == "AI@ SmartReply":
    st.subheader("Example 1: Project Status Update (Professional & Concise)")
    st.write("Scenario:")
    example1 = """
Hi, can you share the latest project status update?
"""
    st.code(example1, language="text")
    st.write("Team inputs the incoming message → AI generates a professional, concise reply with progress percentage, timeline, and no major blockers.")
    copy_button(example1, key="smartreply_ex1")

    st.subheader("Example 2: Weekend Catch-up (Friendly & Casual)")
    st.write("Scenario:")
    example2 = """
Hey, are you free to catch up this weekend?
"""
    st.code(example2, language="text")
    st.write("Team inputs the casual message → AI drafts a warm and friendly reply suggesting Saturday afternoon at a coffee shop, while staying open to other ideas.")
    copy_button(example2, key="smartreply_ex2")

    st.subheader("Example 3: Timesheet Reminder (Polite & Professional)")
    st.write("Scenario:")
    example3 = """
Reminder: Please submit your timesheet today.
"""
    st.code(example3, language="text")
    st.write("Team inputs the reminder → AI creates a polite, professional acknowledgment confirming the timesheet has been submitted and thanking for the reminder.")
    copy_button(example3, key="smartreply_ex3")

    st.subheader("Example 4: Delay Explanation (Respectful & Accountable)")
    st.write("Scenario:")
    example4 = """
We noticed some delays in your recent report submissions. Could you explain the reason?
"""
    st.code(example4, language="text")
    st.write("Team inputs the query → AI generates a respectful reply explaining the delay (waiting for client data), assures completion by tomorrow, and highlights steps to avoid recurrence.")
    copy_button(example4, key="smartreply_ex4")

elif module == "AI@ ResumeScreen":
    st.subheader("Example 1: Software Engineer")
    st.write("Job Description:")
    example1 = """
Responsible for developing, testing, and maintaining software applications. 
Works closely with product managers and designers to translate requirements 
into scalable, efficient code. Troubleshoots issues and ensures software quality.
"""
    st.code(example1, language="text")
    st.write("AI reviews resumes against this description → identifies candidates with coding, debugging, and system optimization experience.")
    copy_button(example1, key="resumescreen_ex1")

    st.subheader("Example 2: Marketing Executive")
    st.write("Job Description:")
    example2 = """
Plans and executes marketing campaigns to promote products and services. 
Conducts market research, analyzes customer trends, and manages social media channels. 
Collaborates with sales to drive brand awareness and engagement.
"""
    st.code(example2, language="text")
    st.write("AI reviews resumes against this description → highlights candidates with digital marketing, content creation, and campaign management expertise.")
    copy_button(example2, key="resumescreen_ex2")

    st.subheader("Example 3: Human Resources Officer")
    st.write("Job Description:")
    example3 = """
Handles recruitment, onboarding, and employee relations. 
Ensures policies comply with labor laws and supports staff welfare initiatives. 
Works with management on training programs and workplace culture.
"""
    st.code(example3, language="text")
    st.write("AI reviews resumes against this description → flags candidates experienced in HR operations, compliance, and talent management.")
    copy_button(example3, key="resumescreen_ex3")

elif module == "AI@ Storyline":
    
    st.write("Choose the settings of type of content you would like to create, objective, style and etc from the system.")
    st.write("Enter your text you may consider the following: ")
    
    st.subheader("Example 1: Healthcare / Wellness")
    example1 = """
We noticed some delays in your recent report submissions. Could you explain the reason?
"""
    st.code(example1, language="text")
    copy_button(example1, key="storyline_ex1")

    st.subheader("Example 2: Education / E-Learning")
    example2 = """
Plan and structure video storylines for online courses, tutorials, or educational campaigns. Supports interactive learning content and engaging social media promotions for students or professionals.
"""
    st.code(example2, language="text")

    copy_button(example2, key="storyline_ex2")

