import pandas as pd

from strategy.structure import build_structure
from strategy.trend import detect_trend

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
    {"open": 100, "high": 102, "low": 99, "close": 101},

    # 1 - primeiro HIGH
    {"open": 101, "high": 105, "low": 100, "close": 104},

    # 2
    {"open": 104, "high": 103, "low": 98, "close": 99},

    # 3 - primeiro LOW
    {"open": 99, "high": 101, "low": 95, "close": 97},

    # 4
    {"open": 97, "high": 104, "low": 96, "close": 103},

    # 5 - segundo HIGH → maior
    {"open": 103, "high": 110, "low": 102, "close": 108},

    # 6
    {"open": 108, "high": 106, "low": 101, "close": 103},

    # 7 - segundo LOW → maior
    {"open": 103, "high": 105, "low": 98, "close": 100},

    # 8
    {"open": 100, "high": 108, "low": 101, "close": 107},

    # 9 - terceiro HIGH → maior
    {"open": 107, "high": 115, "low": 106, "close": 113},

    # 10
    {"open": 113, "high": 111, "low": 104, "close": 106},

    # 11 - terceiro LOW → maior
    {"open": 106, "high": 109, "low": 100, "close": 102},

    # 12
    {"open": 102, "high": 113, "low": 103, "close": 111},

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