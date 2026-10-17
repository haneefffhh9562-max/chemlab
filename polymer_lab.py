import streamlit as st
import plotly.graph_objects as go

POLYMERS = {
    "PET": {
        "full": "Polyethylene terephthalate",
        "repeat": "Simplified repeat unit: [–O–CH₂–CH₂–O–CO–C₆H₄–CO–]ₙ",
        "uses": "Beverage bottles, food packaging and polyester fibres",
        "properties": "Often transparent and strong; recycling depends on collection and processing systems.",
        "end": "PET can be mechanically recycled in suitable systems. It is not generally considered readily biodegradable in ordinary environments.",
        "color": "#42d4c4",
        "stiffness": 75,
        "heat": 70,
    },
    "PVC": {
        "full": "Polyvinyl chloride",
        "repeat": "Simplified repeat unit: [–CH₂–CHCl–]ₙ",
        "uses": "Pipes, cable insulation, flooring and some medical products",
        "properties": "Properties vary with formulation; rigid and flexible grades are both common.",
        "end": "Recycling is technically possible but depends on additives, collection and local facilities.",
        "color": "#66a9ff",
        "stiffness": 80,
        "heat": 60,
    },
    "PLA": {
        "full": "Polylactic acid",
        "repeat": "Simplified repeat unit: [–O–CH(CH₃)–CO–]ₙ",
        "uses": "Some packaging, 3D-printing filament and compostable products",
        "properties": "Can be made from renewable feedstocks; properties depend on grade and processing.",
        "end": "Many PLA products require controlled industrial composting conditions. Biobased does not automatically mean home-compostable.",
        "color": "#e9b86c",
        "stiffness": 65,
        "heat": 45,
    },
}

def render_polymer_lab():
    st.title("🧬 Polymer Explorer")
    st.write("Compare common polymers and explore their structure, uses, and end-of-life considerations.")
    choice = st.selectbox("Select polymer", list(POLYMERS.keys()))
    p = POLYMERS[choice]

    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#16374b,#111f34);border:1px solid {p['color']}66;
    border-radius:18px;padding:20px;margin-bottom:12px">
      <div style="font-size:13px;color:{p['color']};letter-spacing:2px">POLYMER MATERIAL</div>
      <h2 style="margin:5px 0">{choice}</h2>
      <p style="margin:0;color:#b8d1df">{p['full']}</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Simplified repeating unit")
    st.code(p["repeat"])
    st.caption("Text formula is simplified for learning; the subscript n indicates a repeating chain.")

    # Stylized chain diagram, not an atom-accurate molecular model.
    x = list(range(1, 9))
    y = [0.12, -0.12, 0.12, -0.12, 0.12, -0.12, 0.12, -0.12]
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y, mode="lines+markers",
        line=dict(color=p["color"], width=5),
        marker=dict(size=15, color=p["color"], line=dict(color="#eaf8ff", width=1)),
        hovertemplate="Illustrative chain segment<extra></extra>"
    ))
    fig.update_layout(template="plotly_dark", height=190, showlegend=False,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(l=10,r=10,t=10,b=10),
                      xaxis=dict(visible=False), yaxis=dict(visible=False))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Material profile")
    st.write("**Common uses:** " + p["uses"])
    st.write("**Properties:** " + p["properties"])
    st.write("**Recycling / biodegradation:** " + p["end"])

    st.subheader("Compare the polymers")
    rows = []
    for name, item in POLYMERS.items():
        rows.append({"Polymer": name, "Full name": item["full"], "Common uses": item["uses"]})
    st.dataframe(rows, use_container_width=True, hide_index=True)
    st.info("The chain illustration is schematic, not a true 3D molecular structure. Material properties vary by grade, additives and processing.")
