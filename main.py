import pandas as pd

from config import MIN_RR
from strategy.structure import build_structure
from strategy.trend import detect_trend
from strategy.breakout import check_breakout
from strategy.pivots import identify_pivots
from strategy.retest import check_retest

from strategy.support_resistance import (
    create_zones,
    merge_zones
    )

from strategy.price_action import (
    candle_anatomy,
    is_hammer,
    is_inverted_hammer,
    is_doji,
    is_bullish_engulfing,
    is_bearish_engulfing,
    detect_candle_pattern
)

from strategy.volume import (
    average_volume,
    volume_ratio,
    is_volume_confirmed
)

from strategy.volume import (
    average_volume,
    volume_ratio,
    is_volume_confirmed,
    is_confirmation_volume
)

from strategy.setup import evaluate_setup

from risk.position_size import calculate_position_size

from risk.stop_loss import calculate_stop_loss

from risk.take_profit import calculate_take_profit

from risk.risk_manager import calculate_trade_risk

from backtest.statistics import (
    total_trades,
    winning_trades,
    losing_trades,
    total_profit,
    win_rate
)

from backtest.statistics import (
    total_trades,
    winning_trades,
    losing_trades,
    total_profit,
    win_rate,
    profit_factor,
    largest_win,
    largest_loss,
    average_profit
)

from backtest.engine import BacktestEngine


# -----------------------------------------
# DADOS DE TESTE
# -----------------------------------------

data = [

    # 0
    {"open": 100, "high": 102, "low": 99, "close": 101, "volume": 1000},

    # 1 - primeiro HIGH
    {"open": 101, "high": 105, "low": 100, "close": 104, "volume": 1000},

    # 2
    {"open": 104, "high": 103, "low": 98, "close": 99, "volume": 1000},

    # 3 - primeiro LOW
    {"open": 99, "high": 101, "low": 95, "close": 97, "volume": 1000},

    # 4
    {"open": 97, "high": 104, "low": 96, "close": 103, "volume": 1000},

    # 5 - segundo HIGH
    {"open": 103, "high": 110, "low": 102, "close": 108, "volume": 1000},

    # 6
    {"open": 108, "high": 106, "low": 101, "close": 103, "volume": 1000},

    # 7 - segundo LOW
    {"open": 103, "high": 105, "low": 98, "close": 100, "volume": 1000},

    # 8
    {"open": 100, "high": 108, "low": 101, "close": 107, "volume": 1000},

    # 9 - terceiro HIGH
    {"open": 107, "high": 115, "low": 106, "close": 113, "volume": 1000},

    # 10
    {"open": 113, "high": 111, "low": 104, "close": 106, "volume": 1000},

    # 11 - terceiro LOW
    {"open": 106, "high": 109, "low": 100, "close": 102, "volume": 1000},

    # 12
    {"open": 102, "high": 113, "low": 103, "close": 111, "volume": 1000},

    # 13 - rompimento da resistência
    {"open": 110, "high": 114, "low": 109, "close": 113, "volume": 3000},

    # 14
    {"open": 110, "high": 111, "low": 107, "close": 109, "volume": 1000},

    # 15
    {"open": 109, "high": 111, "low": 108, "close": 110, "volume": 1000},

    # 16
    {"open": 110, "high": 112, "low": 109, "close": 111, "volume": 1000},

    # 17
    {"open": 111, "high": 112, "low": 109, "close": 110, "volume": 1000},

    # 18
    {"open": 110, "high": 111, "low": 108, "close": 109, "volume": 1000},

    # 19
    {"open": 109, "high": 111, "low": 108, "close": 110, "volume": 1000},

    # 20
    {"open": 110, "high": 112, "low": 109, "close": 111, "volume": 1000},

    # 21 - ROMPIMENTO
    {"open": 111, "high": 114, "low": 110, "close": 113, "volume": 3000},

    # 22 - FALSO ROMPIMENTO
{
    "open": 109,
    "high": 113,
    "low": 108,
    "close": 110,
    "volume": 3000
},

    # 23
    {"open": 109, "high": 110, "low": 106, "close": 108, "volume": 1000},

    # 24
    {"open": 108, "high": 109, "low": 105, "close": 106, "volume": 1000},

    # 25
    {"open": 106, "high": 107, "low": 102, "close": 103, "volume": 1000},

    # 26
    {"open": 103, "high": 104, "low": 99, "close": 100, "volume": 1000},

    # 27
    {"open": 100, "high": 101, "low": 96, "close": 97, "volume": 1000},

    # 28
    {"open": 97, "high": 98, "low": 94, "close": 95, "volume": 1000},

    # 29
    {"open": 95, "high": 96, "low": 92, "close": 93, "volume": 1000},

    # 30 - ROMPIMENTO DO SUPORTE
    {
      "open": 93,
      "high": 94,
      "low": 90,
      "close": 92,
      "volume": 3000
     },

     # TESTE DE RETESTE

{
    "open": 113,
    "high": 114,
    "low": 110.00,
    "close": 111.50,
    "volume": 1800
},



]


df = pd.DataFrame(data)
df = identify_pivots(df)


# -----------------------------------------
# CONSTRUIR ESTRUTURA
# -----------------------------------------

structure = build_structure(df)

zones = create_zones(df)

zones = merge_zones(zones)



# -----------------------------------------
# MOSTRAR ESTRUTURA
# -----------------------------------------

print("\n===== ESTRUTURA =====\n")

for item in structure:

    print(
        f"Candle {item['index']} "
        f"| {item['type']} "
        f"| preço = {item['price']}"
    )


# -----------------------------------------
# DETECTAR TENDÊNCIA
# -----------------------------------------

trend = detect_trend(structure)


print("\n===== TENDÊNCIA =====\n")

print(
    f"Tendência atual: {trend}"
)

print("\n===== REGIÕES AGRUPADAS =====\n")

for zone in zones:

    print(
        f"{zone['type']} "
        f"| preço = {zone['price']:.2f} "
        f"| região = "
        f"{zone['lower']:.2f} "
        f"até "
        f"{zone['upper']:.2f}"
    )

print("\n===== TESTE DE ROMPIMENTO =====\n")

for index in range(len(df)):

    for zone in zones:

        result = check_breakout(
            df,
            index,
            zone
        )

        if result != "NO_BREAKOUT":

            print(
                f"Candle {index} | "
                f"{zone['type']} | "
                f"Resultado = {result}"
            )

print("\n===== TESTE DE RETESTE =====\n")

# -----------------------------------------
# TESTE DE RETESTE
# -----------------------------------------

for zone in zones:

    if zone["type"] == "RESISTANCE":

        result = check_retest(
            df,
            21,
            zone,
            "BREAKOUT_UP"
        )

        print(
            f"Zona {zone['price']:.2f} | "
            f"Resultado = {result['result']} | "
            f"Candle = {result['index']}"
        )

print("\n===== TESTE DE RETESTE SEM REJEIÇÃO =====\n")

test_data = [

    # Candle 0 = rompimento
    {
        "open": 110,
        "high": 114,
        "low": 109,
        "close": 113,
        "volume": 3000
    },

    # Candle 1 = volta para a zona,
    # mas fecha dentro dela
    {
        "open": 112,
        "high": 113,
        "low": 109.80,
        "close": 110.10,
        "volume": 1000
    }
]

test_df = pd.DataFrame(test_data)

for zone in zones:

    if zone["type"] == "RESISTANCE" and zone["price"] == 110:

        result = check_retest(
            test_df,
            0,
            zone,
            "BREAKOUT_UP"
        )

        print(
            f"Zona {zone['price']:.2f} | "
            f"Resultado = {result['result']}"
        )

print("\n===== TESTE PRICE ACTION =====\n")

# -----------------------------------------
# CANDLE DE TESTE
# -----------------------------------------

candle = {
    "open": 100,
    "high": 105,
    "low": 95,
    "close": 100.5
}

anatomy = candle_anatomy(candle)

print("Anatomia do candle:")

print(
    f"Corpo: {anatomy['body']}"
)

print(
    f"Pavio superior: {anatomy['upper_wick']}"
)

print(
    f"Pavio inferior: {anatomy['lower_wick']}"
)

print(
    f"Range: {anatomy['range']}"
)

print("\nClassificação:")

print(
    f"Martelo: {is_hammer(candle)}"
)

print(
    f"Martelo invertido: "
    f"{is_inverted_hammer(candle)}"
)

print(
    f"Doji: {is_doji(candle)}"
)

print("\n===== TESTE ENGOLFO DE ALTA =====\n")

previous = {
    "open": 105,
    "high": 106,
    "low": 99,
    "close": 100
}

current = {
    "open": 99,
    "high": 108,
    "low": 98,
    "close": 107
}

print(
    "Engolfo de alta:",
    is_bullish_engulfing(previous, current)
)

print(
    "Engolfo de baixa:",
    is_bearish_engulfing(previous, current)
)

print(
    "Padrão identificado:",
    detect_candle_pattern(previous, current)
)

print("\n===== TESTE ENGOLFO DE BAIXA =====\n")

previous = {
    "open": 100,
    "high": 106,
    "low": 99,
    "close": 105
}

current = {
    "open": 106,
    "high": 107,
    "low": 97,
    "close": 98
}

print(
    "Engolfo de alta:",
    is_bullish_engulfing(previous, current)
)

print(
    "Engolfo de baixa:",
    is_bearish_engulfing(previous, current)
)

print(
    "Padrão identificado:",
    detect_candle_pattern(previous, current)
)

print("\n===== TESTE DE VOLUME =====\n")

volume_data = []

# 20 candles com volume normal
for i in range(20):

    volume_data.append({
        "open": 100,
        "high": 101,
        "low": 99,
        "close": 100,
        "volume": 1000
    })


# Candle 20 = volume normal
volume_data.append({
    "open": 100,
    "high": 101,
    "low": 99,
    "close": 100,
    "volume": 1000
})


# Candle 21 = volume forte
volume_data.append({
    "open": 100,
    "high": 103,
    "low": 99,
    "close": 102,
    "volume": 1500
})


# Candle 22 = volume muito forte
volume_data.append({
    "open": 100,
    "high": 105,
    "low": 98,
    "close": 104,
    "volume": 3000
})


volume_df = pd.DataFrame(volume_data)


for index in [20, 21, 22]:

    avg = average_volume(
        volume_df,
        index
    )

    ratio = volume_ratio(
        volume_df,
        index
    )

    confirmed = is_volume_confirmed(
        volume_df,
        index,
        multiplier=1.5
    )

    print(
        f"Candle {index} | "
        f"Volume = {volume_df.iloc[index]['volume']} | "
        f"Média = {avg:.2f} | "
        f"Ratio = {ratio:.2f}x | "
        f"Confirmado = {confirmed}"
    )

print("\n===== TESTE DE VOLUME DE CONFIRMAÇÃO =====\n")

for index in [20, 21, 22]:

    ratio = volume_ratio(
        volume_df,
        index
    )

    confirmed = is_confirmation_volume(
        volume_df,
        index
    )

    print(
        f"Candle {index} | "
        f"Ratio = {ratio:.2f}x | "
        f"Confirmação = {confirmed}"
    )

print("\n===== TESTE DO SETUP =====\n")


# -----------------------------------------
# SETUP DE COMPRA
# -----------------------------------------

result_buy = evaluate_setup(
    trend="UPTREND",
    breakout="BREAKOUT_UP",
    retest="RETEST_UP",
    price_action="HAMMER",
    volume_confirmed=True
)

print(
    f"Setup de compra: {result_buy}"
)


# -----------------------------------------
# SETUP DE VENDA
# -----------------------------------------

result_sell = evaluate_setup(
    trend="DOWNTREND",
    breakout="BREAKOUT_DOWN",
    retest="RETEST_DOWN",
    price_action="BEARISH_ENGULFING",
    volume_confirmed=True
)

print(
    f"Setup de venda: {result_sell}"
)


# -----------------------------------------
# SETUP INCOMPLETO
# -----------------------------------------

result_no_trade = evaluate_setup(
    trend="UPTREND",
    breakout="BREAKOUT_UP",
    retest="NO_RETEST",
    price_action="HAMMER",
    volume_confirmed=False
)

print(
    f"Setup incompleto: {result_no_trade}"
)

print("\n===== TESTE SETUP SEM VOLUME =====\n")

result_no_volume = evaluate_setup(
    trend="UPTREND",
    breakout="BREAKOUT_UP",
    retest="RETEST_UP",
    price_action="HAMMER",
    volume_confirmed=False
)

print(
    f"Setup sem volume: {result_no_volume}"
)

print("\n===== TESTE POSITION SIZE =====\n")


capital = 100.00

entry_price = 100.00

stop_price = 98.00


quantity = calculate_position_size(
    capital,
    entry_price,
    stop_price
)


risk_amount = (
    capital *
    0.01
)


print(
    f"Capital: R$ {capital:.2f}"
)

print(
    f"Entrada: R$ {entry_price:.2f}"
)

print(
    f"Stop: R$ {stop_price:.2f}"
)

print(
    f"Risco máximo: R$ {risk_amount:.2f}"
)

print(
    f"Quantidade calculada: {quantity:.4f}"
)

print("\n===== TESTE POSITION SIZE — STOP PRÓXIMO =====\n")

capital = 100.00

entry_price = 100.00

stop_price = 99.99


quantity = calculate_position_size(
    capital,
    entry_price,
    stop_price
)


print(
    f"Entrada: R$ {entry_price:.2f}"
)

print(
    f"Stop: R$ {stop_price:.2f}"
)

print(
    f"Quantidade calculada: {quantity:.4f}"
)


print("\n===== TESTE STOP LOSS =====\n")


buy_zone = {
    "type": "RESISTANCE",
    "price": 110.00,
    "lower": 109.67,
    "upper": 110.33
}


entry_price = 113.00


stop_buy = calculate_stop_loss(
    entry_price,
    buy_zone,
    "BUY"
)


print(
    f"Entrada BUY: R$ {entry_price:.2f}"
)

print(
    f"Região: "
    f"{buy_zone['lower']:.2f} "
    f"até "
    f"{buy_zone['upper']:.2f}"
)

print(
    f"Stop Loss: R$ {stop_buy:.2f}"
)

print("\n===== TESTE STOP LOSS SELL =====\n")


sell_zone = {
    "type": "SUPPORT",
    "price": 95.00,
    "lower": 94.72,
    "upper": 95.28
}


entry_price = 92.00


stop_sell = calculate_stop_loss(
    entry_price,
    sell_zone,
    "SELL"
)


print(
    f"Entrada SELL: R$ {entry_price:.2f}"
)

print(
    f"Região: "
    f"{sell_zone['lower']:.2f} "
    f"até "
    f"{sell_zone['upper']:.2f}"
)

print(
    f"Stop Loss: R$ {stop_sell:.2f}"
)

print("\n===== TESTE TAKE PROFIT BUY =====\n")


entry_price = 113.00

stop_price = 109.67


take_profit = calculate_take_profit(
    entry_price,
    stop_price,
    "BUY"
)


risk_distance = abs(
    entry_price - stop_price
)


print(
    f"Entrada: R$ {entry_price:.2f}"
)

print(
    f"Stop: R$ {stop_price:.2f}"
)

print(
    f"Risco: R$ {risk_distance:.2f}"
)

print(
    f"R:R configurado: 1:{MIN_RR:.0f}"
)

print(
    f"Take Profit: R$ {take_profit:.2f}"
)

print("\n===== TESTE TAKE PROFIT SELL =====\n")


entry_price = 92.00

stop_price = 95.28


take_profit = calculate_take_profit(
    entry_price,
    stop_price,
    "SELL"
)


risk_distance = abs(
    entry_price - stop_price
)


print(
    f"Entrada: R$ {entry_price:.2f}"
)

print(
    f"Stop: R$ {stop_price:.2f}"
)

print(
    f"Risco: R$ {risk_distance:.2f}"
)

print(
    f"R:R configurado: 1:{MIN_RR:.0f}"
)

print(
    f"Take Profit: R$ {take_profit:.2f}"
)

print("\n===== TESTE INTEGRAÇÃO DO RISCO =====\n")


capital = 100.00

entry_price = 113.00

zone = {
    "type": "RESISTANCE",
    "price": 110.00,
    "lower": 109.67,
    "upper": 110.33
}


trade = calculate_trade_risk(
    capital,
    entry_price,
    zone,
    "BUY"
)


print(
    f"Direção: {trade['direction']}"
)

print(
    f"Entrada: R$ {trade['entry']:.2f}"
)

print(
    f"Stop Loss: R$ {trade['stop']:.2f}"
)

print(
    f"Take Profit: R$ {trade['target']:.2f}"
)

print(
    f"Quantidade: {trade['quantity']:.4f}"
)

print(
    f"Risco financeiro: R$ {trade['risk_amount']:.2f}"
)

print(
    f"Retorno potencial: R$ {trade['reward_amount']:.2f}"
)

print(
    f"R:R: 1:{trade['risk_reward']:.2f}"
)

print("\n===== TESTE DE ESTATÍSTICAS =====\n")


test_trades = [

    {
        "profit": 2.00
    },

    {
        "profit": -1.00
    },

    {
        "profit": 3.00
    },

    {
        "profit": -0.50
    },

    {
        "profit": 1.50
    }
]


print(
    f"Total de trades: "
    f"{total_trades(test_trades)}"
)

print(
    f"Trades vencedores: "
    f"{winning_trades(test_trades)}"
)

print(
    f"Trades perdedores: "
    f"{losing_trades(test_trades)}"
)

print(
    f"Lucro total: "
    f"R$ {total_profit(test_trades):.2f}"
)

print(
    f"Win Rate: "
    f"{win_rate(test_trades):.2f}%"
)

print("\n===== TESTE DE ESTATÍSTICAS =====\n")

print(
    f"Profit Factor: "
    f"{profit_factor(test_trades):.2f}"
)

print(
    f"Maior ganho: "
    f"R$ {largest_win(test_trades):.2f}"
)

print(
    f"Maior perda: "
    f"R$ {largest_loss(test_trades):.2f}"
)

print(
    f"Média por operação: "
    f"R$ {average_profit(test_trades):.2f}"
)

print("\n===== TESTE ENGINE BUY =====\n")

engine = BacktestEngine(100.00)

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=95.00,
    target_price=110.00,
    direction="BUY"
)

engine.close_position(
    exit_price=110.00,
    reason="TARGET"
)

print(
    f"Saldo final: "
    f"R$ {engine.balance:.2f}"
)

print(
    f"Lucro: "
    f"R$ {engine.trades[0]['profit']:.2f}"
)

print(
    f"Direção: "
    f"{engine.trades[0]['direction']}"
)

print("\n===== TESTE ENGINE SELL =====\n")

engine = BacktestEngine(100.00)

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=105.00,
    target_price=90.00,
    direction="SELL"
)

engine.close_position(
    exit_price=90.00,
    reason="TARGET"
)

print(
    f"Saldo final: "
    f"R$ {engine.balance:.2f}"
)

print(
    f"Lucro: "
    f"R$ {engine.trades[0]['profit']:.2f}"
)

print(
    f"Direção: "
    f"{engine.trades[0]['direction']}"
)

print("\n===== TESTE ENGINE BUY STOP =====\n")

engine = BacktestEngine(100.00)

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=95.00,
    target_price=110.00,
    direction="BUY"
)

candle = {
    "open": 98,
    "high": 101,
    "low": 95,
    "close": 96
}

engine.process_candle(candle)

print(
    f"Saldo final: "
    f"R$ {engine.balance:.2f}"
)

print(
    f"Resultado: "
    f"R$ {engine.trades[0]['profit']:.2f}"
)

print(
    f"Motivo: "
    f"{engine.trades[0]['reason']}"
)

print("\n===== TESTE ENGINE SELL STOP =====\n")

engine = BacktestEngine(100.00)

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=105.00,
    target_price=90.00,
    direction="SELL"
)

candle = {
    "open": 102,
    "high": 105,
    "low": 99,
    "close": 104
}

engine.process_candle(candle)

print(
    f"Saldo final: "
    f"R$ {engine.balance:.2f}"
)

print(
    f"Resultado: "
    f"R$ {engine.trades[0]['profit']:.2f}"
)

print(
    f"Motivo: "
    f"{engine.trades[0]['reason']}"
)

print("\n===== TESTE BACKTEST + ESTATÍSTICAS =====\n")


engine = BacktestEngine(100.00)


# =========================================
# TRADE 1 - BUY / TARGET
# =========================================

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=95.00,
    target_price=110.00,
    direction="BUY"
)

candle = {
    "open": 105,
    "high": 110,
    "low": 104,
    "close": 109
}

engine.process_candle(candle)


# =========================================
# TRADE 2 - BUY / STOP
# =========================================

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=95.00,
    target_price=110.00,
    direction="BUY"
)

candle = {
    "open": 98,
    "high": 101,
    "low": 95,
    "close": 96
}

engine.process_candle(candle)


# =========================================
# TRADE 3 - SELL / TARGET
# =========================================

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=105.00,
    target_price=90.00,
    direction="SELL"
)

candle = {
    "open": 95,
    "high": 96,
    "low": 90,
    "close": 91
}

engine.process_candle(candle)


# =========================================
# TRADE 4 - SELL / STOP
# =========================================

engine.open_position(
    entry_price=100.00,
    quantity=0.10,
    stop_price=105.00,
    target_price=90.00,
    direction="SELL"
)

candle = {
    "open": 102,
    "high": 105,
    "low": 99,
    "close": 104
}

engine.process_candle(candle)


# =========================================
# RESULTADOS
# =========================================

trades = engine.trades


print(
    f"Saldo inicial: "
    f"R$ {engine.initial_balance:.2f}"
)

print(
    f"Saldo final: "
    f"R$ {engine.balance:.2f}"
)

print(
    f"Total de trades: "
    f"{total_trades(trades)}"
)

print(
    f"Trades vencedores: "
    f"{winning_trades(trades)}"
)

print(
    f"Trades perdedores: "
    f"{losing_trades(trades)}"
)

print(
    f"Lucro total: "
    f"R$ {total_profit(trades):.2f}"
)

print(
    f"Win Rate: "
    f"{win_rate(trades):.2f}%"
)

print(
    f"Profit Factor: "
    f"{profit_factor(trades):.2f}"
)