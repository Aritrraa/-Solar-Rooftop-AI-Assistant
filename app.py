import streamlit as st
from analyze_image import analyze_image
from report_generator import generate_report
from PIL import Image
import os
import pandas as pd
import altair as alt

# ---- Page Setup ----
st.set_page_config(page_title="☀️ Solar Rooftop AI Assistant", layout="wide")

# ---- Global Styles ----
def inject_global_styles():
    font_size = "18px"
    font_family = "Segoe UI, sans-serif"

    st.markdown(
        f"""
        <style>
            html, body, [class*="css"] {{
                font-size: {font_size};
                font-family: {font_family};
            }}
            .report-style {{
                background-color: #fff8dc;
                color: #000000;
                padding: 1rem;
                border-radius: 10px;
                margin-top: 1rem;
            }}
            .stButton>button {{
                font-size: 18px !important;
                padding: 0.6rem 1.2rem;
                border-radius: 8px;
            }}
            .stDownloadButton>button {{
                font-size: 16px !important;
                border-radius: 6px;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

inject_global_styles()

# ---- App Header ----
st.title("☀️ Solar Rooftop AI Assistant")
st.write("Upload a satellite rooftop image to analyze its solar panel potential.")

# ---- Image Upload ----
uploaded_file = st.file_uploader("📤 Upload a rooftop image", type=["jpg", "png", "jpeg","webp"])

# ---- Initialize history ----
if 'history' not in st.session_state:
    st.session_state.history = []

# ---- Clear History Button ----
if st.sidebar.button("🧹 Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared!")

# ---- Process Uploaded Image ----
if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(image, caption="📷 Uploaded Rooftop", use_container_width=True)

    with st.spinner("🔍 Analyzing rooftop for solar feasibility..."):
        analysis_result = analyze_image(image)
        report_text = generate_report(analysis_result)

    st.success("✅ Analysis Complete!")

    # Save to session history
    st.session_state.history.append({
        "filename": uploaded_file.name,
        "result": analysis_result,
        "report": report_text
    })

    # Summary
    st.markdown("### 📊 Rooftop Solar Potential Summary")
    col2.json(analysis_result)

    # Chart Data
    chart_data = {
        "Metric": [
            "Number of Panels",
            "Installed Capacity (kW)",
            "Annual Energy Output (kWh)",
            "Estimated Cost (USD)",
            "Annual Savings (USD)",
            "ROI (years)"
        ],
        "Value": [
            analysis_result["num_panels"],
            analysis_result["kw_installed"],
            analysis_result["annual_output_kwh"],
            analysis_result["estimated_cost_usd"],
            analysis_result["savings_per_year_usd"],
            analysis_result["roi_years"]
        ]
    }

    df = pd.DataFrame(chart_data)

    st.markdown("### 📈 Solar Metrics Visualization")
    chart = alt.Chart(df).mark_bar(
        cornerRadiusTopLeft=6,
        cornerRadiusTopRight=6
    ).encode(
        x=alt.X('Metric', sort=None, axis=alt.Axis(labelAngle=-20)),
        y=alt.Y('Value'),
        color=alt.value('#f4b400'),
        tooltip=['Metric', 'Value']
    ).properties(
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    # Report
    st.markdown("### 📝 Installation Report")
    st.markdown(f"<div class='report-style'>{report_text}</div>", unsafe_allow_html=True)

    st.download_button("📄 Download Full Report", data=report_text, file_name="solar_report.txt", mime="text/plain")

# ---- History Viewer ----
if st.session_state.history:
    st.markdown("---")
    st.markdown("## 🕓 Previous Analyses")
    for idx, entry in enumerate(reversed(st.session_state.history[-5:])):
        with st.expander(f"📁 {entry['filename']} - View Summary"):
            st.json(entry["result"])
            st.markdown(f"<div class='report-style'>{entry['report']}</div>", unsafe_allow_html=True)
