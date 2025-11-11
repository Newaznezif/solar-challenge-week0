import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Solar Data Discovery",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR ---
st.sidebar.header("🌍 Dashboard Controls 🌍 ")

country = st.sidebar.selectbox("Select a Country:", ["Togo", "Benin", "Sierra Leone"])
file_map = {
  
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierraleone_clean.csv",
    "Togo": "data/togo_clean.csv",
}

file_path = file_map[country]

# --- LOAD DATA ---
if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    # --- MAIN DASHBOARD TITLE ---
    st.title(f"☀️ Solar Data Dashboard ☀️ {country}")
    st.markdown(f"Explore solar energy insights for **{country}**. Use the filters to analyze patterns and metrics.")

    # --- QUICK METRICS ---
    st.subheader("📊 Key Metrics")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", f"{len(df):,}")
    if "GHI" in df.columns:
        col2.metric("Avg. Global Horizontal Irradiance (GHI)", f"{df['GHI'].mean():.2f} W/m²")
    if "Temperature" in df.columns:
        col3.metric("Avg. Temperature", f"{df['Temperature'].mean():.2f} °C")

    # --- FILTERS ---
    st.sidebar.markdown("### 🔍 Filter Data")
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    selected_col = st.sidebar.selectbox("Choose a numeric column to visualize:", numeric_cols)

    # Range slider for filtering numeric values
    min_val, max_val = float(df[selected_col].min()), float(df[selected_col].max())
    value_range = st.sidebar.slider(f"Filter {selected_col}:", min_val, max_val, (min_val, max_val))
    filtered_df = df[(df[selected_col] >= value_range[0]) & (df[selected_col] <= value_range[1])]

    # --- VISUALIZATIONS ---
    st.subheader(f"📈 {selected_col} Distribution")
    fig = px.histogram(
        filtered_df,
        x=selected_col,
        nbins=40,
        color_discrete_sequence=["#FDB813"],
        title=f"Distribution of {selected_col}"
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- CORRELATION HEATMAP ---
    if len(numeric_cols) > 1:
        st.subheader("🔗 Feature Correlation Heatmap")
        corr = df[numeric_cols].corr()
        fig_corr = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            color_continuous_scale="YlOrBr",
            title="Correlation Between Numeric Features"
        )
        st.plotly_chart(fig_corr, use_container_width=True)

    # --- RAW DATA ---
    with st.expander("🧾 View Raw Data"):
        st.dataframe(filtered_df)

else:
    st.error(f"⚠️ File not found: `{file_path}`")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:gray;'>"
    "Built with ❤️ using Streamlit & Plotly | © 2025 Solar Data Discovery Project by Newaz Nezif "
    "</div>",
    unsafe_allow_html=True
)
