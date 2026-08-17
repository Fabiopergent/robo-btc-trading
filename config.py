# ==========================================
# CONFIGURAÇÕES DO ROBÔ BTC - V1
# ==========================================

# -----------------------------
# MERCADO
# -----------------------------

SYMBOL = "BTCUSDT"
TIMEFRAME = "30m"


# -----------------------------
# ESTRUTURA DE MERCADO
# -----------------------------

# Quantidade de candles utilizada
# para identificar pivôs.
PIVOT_CANDLES = 3


# -----------------------------
# SUPORTE E RESISTÊNCIA
# -----------------------------

# Tolerância de 0,3%
ZONE_TOLERANCE = 0.003


# -----------------------------
# ROMPIMENTO
# -----------------------------

# O fechamento precisa ultrapassar
# a região em 0,2%.
BREAKOUT_MARGIN = 0.002


# -----------------------------
# VOLUME
# -----------------------------

# Quantidade de candles utilizada
# para calcular o volume médio.
VOLUME_LOOKBACK = 20

# Volume mínimo para considerar
# um rompimento relevante.
BREAKOUT_VOLUME_MULTIPLIER = 1.5

# Volume mínimo para confirmação
# da retomada.
CONFIRMATION_VOLUME_MULTIPLIER = 1.2


# -----------------------------
# RETESTE
# -----------------------------

# Quantidade máxima de candles para
# o preço realizar o reteste.
MAX_RETEST_CANDLES = 10


# -----------------------------
# RISCO / RETORNO
# -----------------------------

# R:R mínimo de 1:3
MIN_RR = 3.0

# Risco máximo por operação:
# 1% do capital.
RISK_PER_TRADE = 0.01

# Perda máxima diária:
# 3% do capital.
MAX_DAILY_LOSS = 0.03


# -----------------------------
# CAPITAL DA SIMULAÇÃO
# -----------------------------

INITIAL_CAPITAL = 100.00