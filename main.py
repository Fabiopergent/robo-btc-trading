import pandas as pd

from strategy.pivots import identify_pivots


# -----------------------------------------
# DADOS DE TESTE
# -----------------------------------------

data = [
    {"open": 100, "high": 102, "low": 99, "close": 101, "volume": 1000},
    {"open": 101, "high": 103, "low": 100, "close": 102, "volume": 1000},
    {"open": 102, "high": 104, "low": 101, "close": 103, "volume": 1000},

    # Possível Pivot High
    {"open": 103, "high": 110, "low": 102, "close": 109, "volume": 1500},

    {"open": 109, "high": 105, "low": 101, "close": 102, "volume": 1000},
    {"open": 102, "high": 104, "low": 100, "close": 101, "volume": 1000},
    {"open": 101, "high": 103, "low": 99, "close": 100, "volume": 1000},

    # Possível Pivot Low
    {"open": 100, "high": 101, "low": 90, "close": 92, "volume": 1500},

    {"open": 92, "high": 96, "low": 91, "close": 95, "volume": 1000},
    {"open": 95, "high": 98, "low": 93, "close": 97, "volume": 1000},
    {"open": 97, "high": 100, "low": 95, "close": 99, "volume": 1000},
]


df = pd.DataFrame(data)


# -----------------------------------------
# IDENTIFICAR PIVÔS
# -----------------------------------------

df = identify_pivots(df)


# -----------------------------------------
# MOSTRAR RESULTADO
# -----------------------------------------

print("\n===== PIVÔS IDENTIFICADOS =====\n")

for index, row in df.iterrows():

    if row["pivot_high"]:
        print(
            f"Pivot HIGH encontrado no candle {index} "
            f"| máxima = {row['high']}"
        )

    if row["pivot_low"]:
        print(
            f"Pivot LOW encontrado no candle {index} "
            f"| mínima = {row['low']}"
        )