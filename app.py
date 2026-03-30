import streamlit as st

st.set_page_config(layout="wide")

# ======================
# ESTILO PROFISSIONAL
# ======================
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
h1 {
    color: #00ffcc;
    text-align: center;
}
.metric-box {
    background: #1c1f26;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 PAINEL TRADER PRO")

# ======================
# DASHBOARD TOPO
# ======================
col1, col2, col3 = st.columns(3)

col1.markdown('<div class="metric-box">⏱️ 1M<br><b>COMPRA 🟢</b></div>', unsafe_allow_html=True)
col2.markdown('<div class="metric-box">⏱️ 5M<br><b>VENDA 🔴</b></div>', unsafe_allow_html=True)
col3.markdown('<div class="metric-box">⏱️ 15M<br><b>AGUARDAR ⚪</b></div>', unsafe_allow_html=True)

st.markdown("---")

# ======================
# GRÁFICO TRADINGVIEW
# ======================
tradingview_widget = """
<div class="tradingview-widget-container">
  <div id="tv_chart"></div>
  <script src="https://s3.tradingview.com/tv.js"></script>
  <script>
  new TradingView.widget({
    "width": "100%",
    "height": 500,
    "symbol": "BINANCE:BTCUSDT",
    "interval": "1",
    "theme": "dark",
    "style": "1",
    "locale": "br",
    "container_id": "tv_chart"
  });
  </script>
</div>
"""
st.components.v1.html(tradingview_widget, height=550)

st.markdown("---")

# ======================
# ESTRATÉGIA
# ======================
colA, colB = st.columns(2)

with colA:
    st.subheader("🎯 Estratégia")
    st.success("Entrada: Pullback + tendência")
    st.write("Saída: resistência ou alvo")

with colB:
    st.subheader("📍 Região")
    st.info("Zona de suporte forte")

st.markdown("---")

# ======================
# NOTÍCIAS
# ======================
st.subheader("📰 Notícias do Mercado")

st.markdown("""
- Bitcoin sobe com mercado otimista  
- Expectativa de alta no curto prazo  
- Mercado atento a dados econômicos  
""")
