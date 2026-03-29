import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.title("🔥 Painel Profissional BTC")

# ======================
# PEGAR DADOS
# ======================
url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=100"
data = requests.get(url).json()

df = pd.DataFrame(data, columns=[
    "time","open","high","low","close","volume",
    "close_time","qav","trades","tbbav","tbqav","ignore"
])

df["close"] = df["close"].astype(float)

# ======================
# INDICADORES
# ======================
df["ema9"] = df["close"].ewm(span=9).mean()
df["ema21"] = df["close"].ewm(span=21).mean()

# RSI simples
delta = df["close"].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

rs = avg_gain / avg_loss
df["rsi"] = 100 - (100 / (1 + rs))

# ======================
# LÓGICA DE SINAL
# ======================
last = df.iloc[-1]

tendencia = "LATERAL"
sinal = "NEUTRO"
forca = 50

if last["ema9"] > last["ema21"] and last["rsi"] > 55:
    tendencia = "ALTA 📈"
    sinal = "COMPRA 🟢"
    forca = int(last["rsi"])

elif last["ema9"] < last["ema21"] and last["rsi"] < 45:
    tendencia = "BAIXA 📉"
    sinal = "VENDA 🔴"
    forca = int(100 - last["rsi"])

# ======================
# INTERFACE
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("📊 Tendência", tendencia)
col2.metric("🎯 Sinal", sinal)
col3.metric("⚡ Força", f"{forca}%")

st.line_chart(df[["close", "ema9", "ema21"]])

st.subheader("📉 RSI")
st.line_chart(df["rsi"])

st.write("💰 Último preço:", round(last["close"], 2))
