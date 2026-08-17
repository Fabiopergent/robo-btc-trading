import pandas as pd

from strategy.structure import build_structure
from strategy.trend import detect_trend
from strategy.breakout import check_breakout
from strategy.pivots import identify_pivots

from strategy.support_resistance import (
    create_zones,
    merge_zones
)


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