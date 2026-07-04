import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="PrimeTrade Dashboard",
    page_icon="📈",
    layout="wide"
)

# Load Data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "merged_data.csv")

df = pd.read_csv(DATA_PATH)

st.title("📈 PRIME TRADE ANALYSIS DASHBOARD")

st.markdown("---")

# Sidebar
st.sidebar.header("Filters")

coins = ["All"] + sorted(df["Coin"].dropna().unique().tolist())
selected_coin = st.sidebar.selectbox("Select Coin", coins)

sentiments = ["All"] + sorted(df["classification"].dropna().unique().tolist())
selected_sentiment = st.sidebar.selectbox("Market Sentiment", sentiments)

filtered = df.copy()

if selected_coin != "All":
    filtered = filtered[filtered["Coin"] == selected_coin]

if selected_sentiment != "All":
    filtered = filtered[filtered["classification"] == selected_sentiment]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Trades", len(filtered))
col2.metric("Total Profit", f"${filtered['Closed PnL'].sum():,.2f}")
col3.metric("Average Profit", f"${filtered['Closed PnL'].mean():,.2f}")
col4.metric("Win Rate", f"{(filtered['Closed PnL']>0).mean()*100:.2f}%")

st.markdown("---")

# Profit by Sentiment
st.subheader("Average Profit by Market Sentiment")

profit = (
    filtered.groupby("classification")["Closed PnL"]
    .mean()
    .reset_index()
)

fig = px.bar(
    profit,
    x="classification",
    y="Closed PnL",
    color="classification",
    title="Average Profit"
)

st.plotly_chart(fig, use_container_width=True)

# Coin Distribution
st.subheader("Top Coins")

coin = filtered["Coin"].value_counts().head(10).reset_index()
coin.columns = ["Coin", "Trades"]

fig2 = px.bar(
    coin,
    x="Coin",
    y="Trades",
    color="Trades"
)

st.plotly_chart(fig2, use_container_width=True)

# Profit Distribution
st.subheader("Profit Distribution")

fig3 = px.histogram(
    filtered,
    x="Closed PnL",
    nbins=40
)

st.plotly_chart(fig3, use_container_width=True)

# Data Table
st.subheader("Merged Dataset")

st.dataframe(filtered.head(100))

st.markdown("---")
st.caption("PrimeTrade Data Science Project")