
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Kanishk Dawar | Personal Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- THEME TOGGLE ----
theme = st.sidebar.radio("Theme", ["Light", "Dark"])
if theme == "Dark":
    st.markdown(
        "<style>body { background-color: #0E1117; color: white; }</style>",
        unsafe_allow_html=True
    )

# ---- HEADER ----
st.title("Kanishk Dawar")
st.subheader("Brand & Content Strategist")

# ---- DOWNLOAD RESUME ----
resume_path = Path("KanishkDawar_Resume_ATS.pdf")
if resume_path.exists():
    with open(resume_path, "rb") as file:
        st.download_button(
            label="📄 Download Resume (ATS Friendly)",
            data=file,
            file_name="Kanishk_Dawar_Resume.pdf",
            mime="application/pdf"
        )

# ---- ABOUT ----
st.markdown("## About Me")
st.write(
    "Brand & Content Strategist with 2.5+ years of experience driving cultural narratives, "
    "consumer engagement, and data-driven marketing campaigns across education and hospitality sectors."
)

# ---- SKILLS ----
st.markdown("## Skills")
skills = [
    "Brand Strategy", "Brand Positioning", "Content Strategy",
    "Social Media Marketing", "Performance Marketing",
    "Consumer Insights", "Adobe Creative Suite", "MS Office"
]
st.write(", ".join(skills))

# ---- EXPERIENCE ----
st.markdown("## Professional Experience")

with st.expander("Assistant Manager – Marketing | GD Goenka University (Aug 2024 – Nov 2024)"):
    st.write(
        "- Developed brand positioning for Le Cordon Bleu resulting in 25% brand awareness growth\n"
        "- Implemented performance marketing strategies improving ROI by 20%\n"
        "- Led cross-functional brand communication initiatives"
    )

with st.expander("Marketing Executive | Indian School of Hospitality (Aug 2022 – Aug 2024)"):
    st.write(
        "- Managed Instagram, Facebook, LinkedIn & YouTube\n"
        "- Increased engagement and audience growth by 30%\n"
        "- Coordinated internal marketing events and campaigns"
    )

with st.expander("Social Media Coordinator | Camp Land’s End (Mar 2022 – Aug 2022)"):
    st.write(
        "- Built social media presence from scratch\n"
        "- Executed brand awareness and content strategies"
    )

# ---- EDUCATION ----
st.markdown("## Education")
st.write(
    "**Master of Global Business (Marketing)** – SP Jain School of Global Management (2025–2026)  \n"
    "**Bachelor of Culinary Arts Management** – Indian School of Hospitality (2018–2022)  \n"
    "**Bachelor of Travel & Tourism Management** – Maharishi Dayanand University (2018–2022)"
)

# ---- CERTIFICATIONS & AWARDS ----
st.markdown("## Certifications & Awards")
st.write(
    "- Google Fundamentals of Digital Marketing\n"
    "- Basics of SEM – upGrad\n"
    "- Outstanding Effort & Perseverance – ISH\n"
    "- 1st Runner Up – Culinary Student of the Year 2020"
)

st.markdown("---")
st.caption("Built with Streamlit • Portfolio-ready personal dashboard")
