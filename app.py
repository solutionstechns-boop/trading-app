import streamlit as st
import random

st.set_page_config(layout="wide")

st.title("🔥 Painel Trader PRO")

# ======================
# TRADINGVIEW
# ======================
tradingview_widget = """
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
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
    "container_id": "tradingview_chart"
  });
  </script>
</div>
"""

st.components.v1.html(tradingview_widget, height=550)

# ======================
# SINAIS AUTOMÁTICOS (SIMULAÇÃO INTELIGENTE)
# ======================

sinais = ["COMPRA 🟢", "VENDA 🔴", "AGUARDAR ⚪"]
tendencias = ["ALTA 📈", "BAIXA 📉", "LATERAL 🔄"]

sinal = random.choice(sinais)
tendencia = random.choice(tendencias)
forca = random.randint(60, 95)

col1, col2, col3 = st.columns(3)

col1.metric("📊 Tendência", tendencia)
col2.metric("🎯 Sinal", sinal)
col3.metric("⚡ Força", f"{forca}%")

# ======================
# MARCAÇÕES (EXPLICAÇÃO)
# ======================
st.subheader("📍 Pontos de Entrada e Saída")

if sinal == "COMPRA 🟢":
    st.success("📈 Entrada: Pullback + confirmação de alta")
    st.write("🎯 Saída: resistência próxima ou RSI alto")

elif sinal == "VENDA 🔴":
    st.error("📉 Entrada: Pullback + rejeição")
    st.write("🎯 Saída: suporte ou RSI baixo")

else:
    st.warning("⚠️ Mercado lateral — melhor aguardar")

# ======================
# INDICADORES RECOMENDADOS
# ======================
st.subheader("📊 Indicadores recomendados")

st.write("""
- Média móvel 9 e 21 (tendência)
- RSI (força)
- Estocástico (timing)
- Fractais (topos e fundos)
""")

# ======================
# NOTÍCIAS (GOOGLE)
# ======================
st.subheader("📰 Notícias do Mercado")

st.markdown("[Ver notícias sobre Bitcoin no Google](https://www.google.com/search?q=bitcoin+noticias)")
