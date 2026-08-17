import pandas as pd

from config import PIVOT_CANDLES


def is_pivot_high(df, index):
    """
    Verifica se o candle no índice informado
    é um Pivot High.

    Um Pivot High possui máxima maior que as
    máximas dos 3 candles anteriores e dos
    3 candles posteriores.
    """

    n = PIVOT_CANDLES

    # Não temos candles suficientes antes
    if index < n:
        return False

    # Não temos candles suficientes depois
    if index + n >= len(df):
        return False

    current_high = df.iloc[index]["high"]

    # Candles anteriores
    previous_highs = df.iloc[index - n:index]["high"]

    # Candles posteriores
    next_highs = df.iloc[index + 1:index + n + 1]["high"]

    # O máximo atual precisa ser maior que todos
    # os máximos da região analisada.
    return (
        current_high > previous_highs.max()
        and current_high > next_highs.max()
    )


def is_pivot_low(df, index):
    """
    Verifica se o candle no índice informado
    é um Pivot Low.

    Um Pivot Low possui mínima menor que as
    mínimas dos 3 candles anteriores e dos
    3 candles posteriores.
    """

    n = PIVOT_CANDLES

    # Não temos candles suficientes antes
    if index < n:
        return False

    # Não temos candles suficientes depois
    if index + n >= len(df):
        return False

    current_low = df.iloc[index]["low"]

    # Candles anteriores
    previous_lows = df.iloc[index - n:index]["low"]

    # Candles posteriores
    next_lows = df.iloc[index + 1:index + n + 1]["low"]

    return (
        current_low < previous_lows.min()
        and current_low < next_lows.min()
    )


def identify_pivots(df):
    """
    Percorre os candles e identifica Pivot High
    e Pivot Low.

    Retorna uma cópia do DataFrame com duas
    novas colunas:
        pivot_high
        pivot_low
    """

    result = df.copy()

    result["pivot_high"] = False
    result["pivot_low"] = False

    for index in range(len(result)):

        if is_pivot_high(result, index):
            result.loc[result.index[index], "pivot_high"] = True

        if is_pivot_low(result, index):
            result.loc[result.index[index], "pivot_low"] = True

    return result