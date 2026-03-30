import streamlit as st
import random

st.set_page_config(layout="wide")

st.title("🔥 PAINEL TRADER PRO")

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

# ======================
# SINAIS POR TIMEFRAME
# ======================
st.subheader("📊 Sinais por Tempo Gráfico")

def gerar_sinal():
    sinais = ["COMPRA 🟢", "VENDA 🔴", "AGUARDAR ⚪"]
    return random.choice(sinais)

col1, col2, col3 = st.columns(3)

col1.metric("⏱️ 1 Min", gerar_sinal())
col2.metric("⏱️ 5 Min", gerar_sinal())
col3.metric("⏱️ 15 Min", gerar_sinal())

# ======================
# REGIÕES (SIMULAÇÃO)
# ======================
st.subheader("📍 Regiões Importantes")

regioes = [
    "Suporte forte próximo",
    "Resistência sendo testada",
    "Zona de reversão",
    "Região neutra"
]

st.info(random.choice(regioes))

# ======================
# ENTRADA E SAÍDA
# ======================
st.subheader("🎯 Estratégia Atual")

sinal = gerar_sinal()

if "COMPRA" in sinal:
    st.success("Entrada: Pullback + confirmação de alta")
    st.write("Saída: Próxima resistência")

elif "VENDA" in sinal:
    st.error("Entrada: Rejeição + tendência de baixa")
    st.write("Saída: Próximo suporte")

else:
    st.warning("Mercado lateral — aguardar melhor ponto")

# ======================
# NOTÍCIAS
# ======================
st.subheader("📰 Notícias do Mercado")

st.markdown("""
- [Bitcoin sobe com mercado otimista](https://www.google.com/search?q=bitcoin+noticias)
- [Análise do mercado cripto hoje](https://www.google.com/search?q=crypto+market+news)
- [Impacto econômico no BTC](https://www.google.com/search?q=bitcoin+economia)
""")
