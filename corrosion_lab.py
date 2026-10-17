import streamlit as st
import plotly.graph_objects as go

ENVIRONMENTS = {
    "Dry air": {"rate": 0.15, "description": "Limited moisture generally slows ordinary atmospheric rusting."},
    "Moist air": {"rate": 0.55, "description": "Moisture helps electrochemical corrosion processes occur."},
    "Salt water": {"rate": 0.9, "description": "Dissolved salts can increase conductivity and often accelerate corrosion of iron."},
}

def render_corrosion_lab():
    st.title("🔩 Corrosion Simulator")
    st.write("Explore a **conceptual model** of how environment can influence iron corrosion.")
    environment = st.selectbox("Choose environment", list(ENVIRONMENTS.keys()))
    days = st.slider("Illustrative elapsed time (days)", min_value=0, max_value=30, value=10)
    protection = st.selectbox("Surface condition", ["Uncoated iron", "Protective paint coating", "Galvanized coating"])

    base = ENVIRONMENTS[environment]["rate"]
    factor = {"Uncoated iron": 1.0, "Protective paint coating": 0.25, "Galvanized coating": 0.15}[protection]
    index = min(100, round(days * base * factor * 3.2, 1))
    st.caption("The index is a made-up teaching scale, not a measured corrosion rate or a prediction of real metal loss.")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.metric("Illustrative corrosion index", f"{index}/100")
        st.progress(int(index))
        st.markdown(f"**Environment:** {environment}")
        st.write(ENVIRONMENTS[environment]["description"])
        st.write(f"**Surface:** {protection}")
    with col2:
        # Decorative iron coupon with a rust-colored overlay proportional to the index.
        rust_height = max(5, int(index * 0.72))
        st.markdown(f"""
        <div style="height:240px;border-radius:18px;background:linear-gradient(135deg,#122d40,#0b1d2c);
        border:1px solid #356176;display:flex;align-items:center;justify-content:center;overflow:hidden">
          <div style="width:100px;height:175px;border:2px solid #a9bdc9;border-radius:12px;position:relative;
          background:linear-gradient(90deg,#71818a,#b5c1c5,#64737b);overflow:hidden">
            <div style="position:absolute;left:0;right:0;bottom:0;height:{rust_height}%;
            background:repeating-linear-gradient(35deg,#9c4d2d,#9c4d2d 8px,#c17642 8px,#c17642 14px);
            opacity:.9"></div>
          </div>
        </div>
        <p style="text-align:center;color:#a8c6d8;font-size:12px">Illustrative visual only</p>
        """, unsafe_allow_html=True)

    st.subheader("Conceptual comparison")
    rows = []
    for env, item in ENVIRONMENTS.items():
        rows.append({"Environment": env, "Conceptual tendency": ["Lower", "Moderate", "Often higher"][list(ENVIRONMENTS.keys()).index(env)]})
    st.table(rows)

    st.subheader("How can corrosion be reduced?")
    st.markdown("""
    - **Painting/coating:** can limit contact between metal and the environment if the coating remains intact.
    - **Galvanization:** uses a zinc coating to protect steel; zinc can also provide sacrificial protection.
    - **Design and maintenance:** avoid trapped moisture and inspect protective layers.
    """)
    st.info("The visual index is a simple classroom model. Actual corrosion depends on material, temperature, chemistry, oxygen, surface condition, and exposure time.")
