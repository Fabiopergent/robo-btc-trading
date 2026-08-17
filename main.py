import pandas as pd

from strategy.volume import (
    average_volume,
    volume_ratio,
    is_volume_confirmed
)


# -----------------------------------------
# CRIAR DADOS DE TESTE
# -----------------------------------------

data = []

# 20 candles com volume normal
for i in range(20):

    data.append({
        "open": 100,
        "high": 102,
        "low": 98,
        "close": 101,
        "volume": 1000
    })


# Candle atual com volume forte
data.append({
    "open": 101,
    "high": 105,
    "low": 100,
    "close": 104,
    "volume": 2000
})


df = pd.DataFrame(data)


# -----------------------------------------
# TESTE
# -----------------------------------------

index = 20

avg = average_volume(df, index)

ratio = volume_ratio(df, index)

confirmed = is_volume_confirmed(
    df,
    index
)


print("\n===== TESTE DE VOLUME =====\n")

print(f"Volume atual: {df.iloc[index]['volume']}")
print(f"Volume médio: {avg}")
print(f"Relação: {ratio:.2f}x")
print(f"Volume confirmado: {confirmed}")