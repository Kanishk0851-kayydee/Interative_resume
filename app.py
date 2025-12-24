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
# THEME SELECTOR (TOP RIGHT)
# --------------------------------------------------
_, _, theme_col = st.columns([6, 1.5, 1.5])
with theme_col:
    theme = st.selectbox("Theme", ["Dark", "Light"], label_visibility="collapsed")

# --------------------------------------------------
# THEME VARIABLES
# --------------------------------------------------
if theme == "Dark":
    BG = "#0E1117"
    CARD = "#161B22"
    TEXT = "#E6EDF3"
    MUTED = "#9BA3AF"
    ACCENT = "#4FD1C5"
else:
    BG = "#F4F6F8"
    CARD = "#FAFAFA"
    TEXT = "#1A202C"
    MUTED = "#4A5568"
    ACCENT = "#2563EB"

# --------------------------------------------------
# GLOBAL STYLES
# --------------------------------------------------
st.markdown(
    f"""
    <style>
    html, body, [data-testid="stApp"] {{
        background-color: {BG};
        color: {TEXT};
    }}

    .container {{
        max-width: 1100px;
        margin: auto;
    }}

    .card {{
        background-color: {CARD};
        padding: 24px;
        border-radius: 16px;
        margin-bottom: 24px;
        border: 1px solid rgba(0,0,0,0.05);
    }}

    .skill {{
        background-color: {ACCENT};
        color: white;
        padding: 8px 16px;
        border-radius: 999px;
        font-size: 14px;
        display: inline-block;
        margin: 6px;
    }}

    .muted {{
        color: {MUTED};
    }}
    </style>

    <script>
    function animateValue(id, start, end, duration) {{
        const obj = document.getElementById(id);
        let startTimestamp = null;
        const step = (timestamp) => {{
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            obj.innerHTML = Math.floor(progress * (end - start) + start);
            if (progress < 1) {{
                window.requestAnimationFrame(step);
            }}
        }};
        window.requestAnimationFrame(step);
    }}
    </script>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# CONTENT WRAPPER
# --------------------------------------------------
st.markdown("<div class='container'>", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    f"""
    <h1>Kanishk Dawar</h1>
    <h4 class="muted">
    Brand & Content Strategist · Performance Marketing · Consumer Insights
    </h4>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# CTA BUTTONS
# --------------------------------------------------
cta1, cta2 = st.columns([2, 6])

with cta1:
    resume = Path("Kanishk_Dawar_Resume.pdf")
    if resume.exists():
        with open(resume, "rb") as f:
            st.download_button(
                "📄 Download Resume",
                f,
                file_name="Kanishk_Dawar_Resume.pdf"
            )

with cta2:
    st.markdown(
        """
        <a href="https://www.linkedin.com" target="_blank">
        <button style="
            background:#0A66C2;
            color:white;
            padding:10px 18px;
            border:none;
            border-radius:10px;
            cursor:pointer;">
            🔗 Connect on LinkedIn
        </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# --------------------------------------------------
# ABOUT
# --------------------------------------------------
st.markdown("## About Me")
st.markdown(
    """
    <div class="card">
    Brand & Content Strategist with <b>2.5+ years of experience</b> driving cultural narratives,
    engagement, and <b>data-driven marketing campaigns</b> across education and hospitality.
    Strong focus on performance optimization and creative effectiveness.
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
    ✔ Creative strategy + performance marketing<br><br>
    ✔ Proven measurable impact (ROI, awareness, engagement)<br><br>
    ✔ Brand storytelling backed by data<br><br>
    ✔ Experience with premium education & hospitality brands
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# ANIMATED COUNTERS
# --------------------------------------------------
st.markdown("## Impact at a Glance")
st.markdown(
    f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between; text-align:center;">
            <div style="flex:1;">
                <h2 id="exp" style="color:{ACCENT};">0</h2>
                <p class="muted">Years Experience</p>
            </div>
            <div style="flex:1;">
                <h2 id="awareness" style="color:{ACCENT};">0</h2>
                <p class="muted">% Brand Awareness Growth</p>
            </div>
            <div style="flex:1;">
                <h2 id="engagement" style="color:{ACCENT};">0</h2>
                <p class="muted">% Engagement Growth</p>
            </div>
            <div style="flex:1;">
                <h2 id="roi" style="color:{ACCENT};">0</h2>
                <p class="muted">% ROI Improvement</p>
            </div>
        </div>
    </div>

    <script>
        animateValue("exp", 0, 3, 1200);
        animateValue("awareness", 0, 25, 1500);
        animateValue("engagement", 0, 30, 1500);
        animateValue("roi", 0, 20, 1500);
    </script>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SKILLS
# --------------------------------------------------
st.markdown("## Core Skills")
st.markdown("<div class='card'>", unsafe_allow_html=True)

skills = [
    "Brand Strategy", "Brand Positioning", "Content Strategy",
    "Performance Marketing", "Social Media Marketing",
    "Consumer Insights", "Creative Analytics",
    "Adobe Creative Suite", "Microsoft Office"
]

cols = st.columns(3)
for i, skill in enumerate(skills):
    cols[i % 3].markdown(f"<span class='skill'>{skill}</span>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --------------------------------------------------
# PROJECTS
# --------------------------------------------------
st.markdown("## Key Projects")
p1, p2 = st.columns(2)

with p1:
    st.markdown(
        """
        <div class="card">
        <h4>Fan Engagement in Streaming Entertainment</h4>
        <p class="muted">Strategy & Monetization Framework</p>
        Built a data-backed model linking fan engagement to revenue
        for niche streaming platforms.
        </div>
        """,
        unsafe_allow_html=True
    )

with p2:
    st.markdown(
        """
        <div class="card">
        <h4>Nestlé India – B2B Product Innovation</h4>
        <p class="muted">Industry Collaboration</p>
        Conducted demand analysis with hotels & restaurants to
        inform product innovation strategy.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)
st.caption("Interactive Resume • Built with Streamlit")
