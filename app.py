import streamlit as st

st.set_page_config(layout="wide")

st.title("📊 Painel Profissional BTC")

# ======================
# TRADINGVIEW EMBED
# ======================

tradingview_widget = """
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container">
  <div id="tradingview_chart"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget({
  "width": "100%",
  "height": 500,
  "symbol": "BINANCE:BTCUSDT",
  "interval": "1",
  "timezone": "America/Sao_Paulo",
  "theme": "dark",
  "style": "1",
  "locale": "br",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "hide_top_toolbar": false,
  "save_image": false,
  "container_id": "tradingview_chart"
});
  </script>
</div>
<!-- TradingView Widget END -->
"""

st.components.v1.html(tradingview_widget, height=550)

st.write("🔔 Use seu setup direto no gráfico acima")
