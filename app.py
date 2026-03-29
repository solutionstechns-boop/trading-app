import streamlit as st
import requests

st.title("📊 Painel BTC em Tempo Real")

url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
data = requests.get(url).json()

preco = float(data["price"])

st.metric("💰 Preço BTC", f"${preco:,.2f}")
