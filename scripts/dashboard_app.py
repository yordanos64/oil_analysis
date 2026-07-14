import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Birhan Energies Dashboard", layout="wide")

st.title("🛢️ Birhan Energies: Brent Oil Price Analytics Dashboard")
st.markdown("Interactive time series tracking, historical regime shifts, and change point analysis mapping.")

# Load historical oil asset pricing data
data_path = os.path.join(os.path.dirname(__file__), '../data/BrentOilPrices.csv')

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Dashboard Interactive Metric Sidebar Widgets
    st.sidebar.header("Filter Analytics Window")
    year_range = st.sidebar.slider("Select Timeline Range", int(df['Date'].dt.year.min()), int(df['Date'].dt.year.max()), (2010, 2022))
    
    # Filter dataset rows based on slider choices
    filtered_df = df[(df['Date'].dt.year >= year_range[0]) & (df['Date'].dt.year <= year_range[1])]
    
    # Display modern layout cards
    col1, col2 = st.columns(2)
    col1.metric("Max Price in Selected Window", f"${filtered_df['Price'].max():.2f} USD")
    col2.metric("Average Price in Selected Window", f"${filtered_df['Price'].mean():.2f} USD")
    
    # Interactive Timeline Visualization
    st.subheader("Historical Pricing & Trend Baseline")
    st.line_chart(data=filtered_df, x='Date', y='Price', use_container_width=True)
    
    # Documented Historical Change Point Milestones Table
    st.subheader("📍 Detected Structural Break Records")
    breaks_data = {
        "Break Date": ["2020-03-11", "2014-11-27", "2008-09-15"],
        "Attributed Geopolitical Event": ["COVID-19 Pandemic & Price War", "OPEC Production Market Shift", "Lehman Brothers Financial Crisis Collapse"],
        "Pre-Break Mean Price": ["$62.00", "$102.00", "$115.00"],
        "Post-Break Mean Price": ["$31.00", "$48.00", "$55.00"]
    }
    st.table(pd.DataFrame(breaks_data))
    
else:
    st.error("Data file path not resolved. Please verify data/BrentOilPrices.csv is populated.")
