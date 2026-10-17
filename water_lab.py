import streamlit as st
import plotly.graph_objects as go
import pandas as pd

SAMPLES = {
    "Sample A — Neutral example": {"pH": 7.0, "hardness": 90, "turbidity": 1.2, "note": "A near-neutral example with relatively low turbidity."},
    "Sample B — Hard-water example": {"pH": 7.4, "hardness": 260, "turbidity": 2.0, "note": "This example has higher hardness, commonly associated with dissolved calcium and magnesium."},
    "Sample C — Acidic example": {"pH": 5.5, "hardness": 55, "turbidity": 1.5, "note": "This example is acidic. Investigate possible causes before drawing conclusions."},
    "Sample D — Cloudy example": {"pH": 7.2, "hardness": 120, "turbidity": 8.0, "note": "This example has elevated turbidity, meaning more suspended particles are represented."},
}

def render_water_lab():
    st.title("💧 Water Quality Explorer")
    st.write("Select a **simulated** water sample and explore three common water-quality parameters.")
    sample_name = st.selectbox("Choose a sample", list(SAMPLES.keys()))
    data = SAMPLES[sample_name]

    st.markdown("### Virtual sample")
    color = "#4bbce8" if data["turbidity"] < 5 else "#b9a16c"
    st.markdown(f"""
    <div style="display:flex;gap:18px;align-items:center;background:linear-gradient(135deg,#15384b,#102234);
    border:1px solid #397a91;border-radius:18px;padding:18px;margin-bottom:15px">
      <div style="width:76px;height:100px;border:3px solid #b5d9e8;border-top:0;border-radius:8px 8px 18px 18px;
      background:linear-gradient(to top,{color}aa 0%,{color}66 72%,transparent 72%);box-shadow:0 0 25px {color}33"></div>
      <div><h3 style="margin:0"> {sample_name} </h3><p style="margin:6px 0;color:#c5dbe8">{data["note"]}</p>
      <small style="color:#8fb4c7">Illustrative digital sample — not a real test</small></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("pH", f'{data["pH"]:.1f}', help="pH describes acidity or basicity.")
    c2.metric("Hardness", f'{data["hardness"]} mg/L', help="Illustrative hardness as CaCO₃ equivalent.")
    c3.metric("Turbidity", f'{data["turbidity"]} NTU', help="Illustrative turbidity reading.")

    st.markdown("### Parameter comparison")
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=["pH (not a concentration)", "Hardness (mg/L)", "Turbidity (NTU)"],
        y=[data["pH"], data["hardness"], data["turbidity"]],
        marker_color=["#45d6c5", "#55a6e8", "#e9b86c"],
        text=[f'{data["pH"]:.1f}', f'{data["hardness"]} mg/L', f'{data["turbidity"]} NTU'],
        textposition="outside"
    ))
    fig.update_layout(template="plotly_dark", height=350, showlegend=False,
                      paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                      margin=dict(l=20,r=20,t=20,b=20), yaxis_title="Displayed value (units differ)")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### What does this mean?")
    st.markdown("""
    - **pH:** values below 7 are acidic, around 7 are neutral, and above 7 are basic at typical reference conditions.
    - **Hardness:** mainly relates to dissolved calcium and magnesium; the displayed value is an illustrative CaCO₃ equivalent.
    - **Turbidity:** describes how much suspended material scatters light.
    """)
    st.warning("This prototype uses predefined simulated values. A real drinking-water assessment requires suitable sampling, calibrated methods, and relevant standards; these three values alone cannot prove water is safe.")
