import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from water_lab import render_water_lab
from corrosion_lab import render_corrosion_lab
from polymer_lab import render_polymer_lab

st.set_page_config(
    page_title="ChemLab 3D | Virtual Engineering Chemistry",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
:root { --accent:#36d6c5; }
.stApp {
    background:
      radial-gradient(circle at 15% 5%, rgba(36,143,165,.20), transparent 28%),
      radial-gradient(circle at 90% 15%, rgba(86,91,180,.18), transparent 30%),
      #08131f;
    color: #edf7ff;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #102637, #0b1724);
    border-right: 1px solid rgba(95,220,220,.25);
}
h1, h2, h3 { color: #e8fbff !important; }
p, label, .stMarkdown { color: #d4e5ef; }
div[data-testid="stMetric"] {
    background: rgba(19,47,65,.65);
    border: 1px solid rgba(83,210,204,.28);
    padding: 15px;
    border-radius: 14px;
}
div.stButton > button {
    border-radius: 10px;
    border: 1px solid #36d6c5;
}
.lab-hero {
    padding: 1.5rem 1.6rem;
    border-radius: 20px;
    border: 1px solid rgba(80,220,210,.35);
    background: linear-gradient(135deg, rgba(21,66,83,.85), rgba(23,32,62,.9));
    box-shadow: 0 12px 35px rgba(0,0,0,.22);
}
.lab-card {
    padding: 1rem;
    border-radius: 16px;
    background: rgba(18,43,60,.72);
    border: 1px solid rgba(110,194,213,.23);
    min-height: 150px;
}
.small-muted { color: #9fb9c9; font-size: .9rem; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🧪 ChemLab 3D")
    st.caption("Virtual Engineering Chemistry Lab")
    page = st.radio(
        "Choose a lab",
        ["🏠 Home", "💧 Water Quality", "🔩 Corrosion", "🧬 Polymers"],
        label_visibility="visible"
    )
    st.divider()
    st.markdown("**Project team**")
    st.caption("Add your team and college details to the project presentation.")
    st.caption("Educational simulation • No real lab measurements")

if page == "🏠 Home":
    st.markdown("""
    <div class="lab-hero">
      <h1>🧪 Welcome to ChemLab 3D</h1>
      <p>Explore engineering chemistry through interactive virtual experiments.</p>
      <p class="small-muted">Water quality • Corrosion • Polymers</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    st.info("Choose a lab from the left menu to begin. All sample readings and visual outcomes in this prototype are simulated for learning.")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="lab-card"><h3>💧 Water Quality</h3><p>Explore pH, hardness and turbidity in sample water profiles.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="lab-card"><h3>🔩 Corrosion</h3><p>Compare illustrative corrosion conditions and prevention methods.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="lab-card"><h3>🧬 Polymer Explorer</h3><p>Compare common polymers, properties and applications.</p></div>', unsafe_allow_html=True)
    st.subheader("Project overview")
    st.markdown("""
    **Goal:** provide an interactive, browser-based chemistry learning tool.

    **Built with:** Python, Streamlit, Plotly and basic CSS styling.

    **Important:** this is an educational model. It does not replace laboratory testing or establish whether water is safe to drink.
    """)
elif page == "💧 Water Quality":
    render_water_lab()
elif page == "🔩 Corrosion":
    render_corrosion_lab()
elif page == "🧬 Polymers":
    render_polymer_lab()

st.divider()
st.caption("ChemLab 3D • Beginner tech-fest prototype • Verify chemistry content with your course references.")
