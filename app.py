import streamlit as st
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Kanishk Dawar | Interactive Resume",
    layout="wide"
)

# --------------------------------------------------
# TOP RIGHT THEME DROPDOWN
# --------------------------------------------------
col1, col2, col3 = st.columns([6, 1.5, 1])
with col3:
    theme = st.selectbox("", ["Light Mode", "Dark Mode"])

# --------------------------------------------------
# THEME STYLES
# --------------------------------------------------
if theme == "Dark Mode":
    bg_color = "#0E1117"
    card_color = "#161B22"
    text_color = "#FAFAFA"
    accent = "#4FD1C5"
else:
    bg_color = "#F7FAFC"
    card_color = "#FFFFFF"
    text_color = "#1A202C"
    accent = "#2B6CB0"

st.markdown(
    f"""
    <style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}
    .card {{
        background-color: {card_color};
        padding: 20px;
        border-radius: 14px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    .skill {{
        display: inline-block;
        background-color: {accent};
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        margin: 6px 6px 0 0;
        font-size: 14px;
    }}
    .metric {{
        font-size: 26px;
        font-weight: bold;
        color: {accent};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    f"""
    <h1 style="margin-bottom:5px;">Kanishk Dawar</h1>
    <h4 style="color:{accent}; margin-top:0;">
    Brand & Content Strategist | Performance Marketing | Consumer Insights
    </h4>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# CTA BUTTONS
# --------------------------------------------------
cta1, cta2, cta3 = st.columns([2, 2, 4])

with cta1:
    resume_path = Path("Kanishk_Dawar_Resume.pdf")
    if resume_path.exists():
        with open(resume_path, "rb") as file:
            st.download_button(
                "📄 Download Resume",
                file,
                file_name="Kanishk_Dawar_Resume.pdf",
                mime="application/pdf"
            )

with cta2:
    st.markdown(
        """
        <a href="https://www.linkedin.com" target="_blank">
        <button style="
            background-color:#0A66C2;
            color:white;
            padding:10px 16px;
            border:none;
            border-radius:8px;
            cursor:pointer;">
            🔗 Connect on LinkedIn
        </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# ABOUT ME
# --------------------------------------------------
st.markdown("## About Me")
st.markdown(
    """
    <div class="card">
    Brand & Content Strategist with **2.5+ years of experience** building cultural narratives,
    driving engagement, and executing **data-driven marketing campaigns** across
    **education and hospitality sectors**. Strong focus on performance optimization,
    creative effectiveness, and brand positioning.
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# WHY HIRE ME
# --------------------------------------------------
st.markdown("## Why Hire Me")
st.markdown(
    """
    <div class="card">
    ✔ I combine **creative strategy + performance marketing** <br><br>
    ✔ I’ve delivered **measurable growth** (ROI, engagement, awareness) <br><br>
    ✔ I understand **brand storytelling backed by data** <br><br>
    ✔ I’ve worked across **premium education & hospitality brands**
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SKILLS
# --------------------------------------------------
st.markdown("## Core Skills")

skills = [
    "Brand Strategy", "Brand Positioning", "Content Strategy",
    "Performance Marketing", "Social Media Marketing",
    "Consumer Insights", "Creative Analytics",
    "Adobe Creative Suite", "Microsoft Office"
]

st.markdown("<div class='card'>", unsafe_allow_html=True)
for skill in skills:
    st.markdown(f"<span class='skill'>{skill}</span>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------
st.markdown("## Professional Experience")

with st.expander("Assistant Manager – Marketing | GD Goenka University (2024)"):
    st.markdown(
        """
        - Built brand positioning for **Le Cordon Bleu**
        - Achieved **25% increase in brand awareness**
        - Improved performance marketing **ROI by 20%**
        - Led cross-functional brand alignment
        """
    )

with st.expander("Marketing Executive | Indian School of Hospitality (2022–2024)"):
    st.markdown(
        """
        - Managed Instagram, Facebook, LinkedIn & YouTube
        - Increased engagement & audience growth by **30%**
        - Executed content calendars & campaign launches
        """
    )

with st.expander("Social Media Coordinator | Camp Land’s End (2022)"):
    st.markdown(
        """
        - Built social presence from scratch
        - Executed brand awareness strategy
        """
    )

# --------------------------------------------------
# PROJECTS WITH METRICS
# --------------------------------------------------
st.markdown("## Key Projects")

p1, p2 = st.columns(2)

with p1:
    st.markdown(
        """
        <div class="card">
        <h4>Fan Engagement in Streaming Entertainment</h4>
        <p>Academic Strategy Project</p>
        <p class="metric">+ Monetization Framework</p>
        <p>Mapped fan engagement tactics to revenue outcomes
        for niche content platforms.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with p2:
    st.markdown(
        """
        <div class="card">
        <h4>Nestlé India – B2B Product Innovation</h4>
        <p>Industry Collaboration</p>
        <p class="metric">Market-Led NPD</p>
        <p>Conducted demand analysis with hotels &
        restaurants to inform product innovation.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# EDUCATION
# --------------------------------------------------
st.markdown("## Education")
st.markdown(
    """
    <div class="card">
    <b>Master of Global Business (Marketing)</b><br>
    SP Jain School of Global Management (2025–2026)<br><br>
    <b>Bachelor of Culinary Arts Management</b><br>
    Indian School of Hospitality (2018–2022)<br><br>
    <b>Bachelor of Travel & Tourism Management</b><br>
    Maharishi Dayanand University (2018–2022)
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Built with Streamlit • Interactive Resume Dashboard")
