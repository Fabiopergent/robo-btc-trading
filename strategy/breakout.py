import pandas as pd

from config import (
    BREAKOUT_MARGIN,
    VOLUME_LOOKBACK,
    BREAKOUT_VOLUME_MULTIPLIER
)


def calculate_average_volume(df, index):
    """
    Calcula o volume médio dos candles anteriores
    ao candle atual.
    """

    lookback = VOLUME_LOOKBACK

    if index < lookback:
        return None

    previous_volumes = df.iloc[
        index - lookback:index
    ]["volume"]

    return previous_volumes.mean()


def check_breakout(df, index, zone):
    """
    Verifica se o candle indicado realizou um
    rompimento válido da região.

    Retorna:
        BREAKOUT_UP
        BREAKOUT_DOWN
        NO_BREAKOUT
    """

    candle = df.iloc[index]

    close = candle["close"]
    volume = candle["volume"]

    zone_upper = zone["upper"]
    zone_lower = zone["lower"]

    average_volume = calculate_average_volume(df, index)

    # Não temos volume histórico suficiente
    if average_volume is None:
        return "NO_BREAKOUT"

    # Volume precisa superar a média
    required_volume = (
        average_volume *
        BREAKOUT_VOLUME_MULTIPLIER
    )

    volume_confirmed = volume >= required_volume

    # -----------------------------------------
    # ROMPIMENTO DE RESISTÊNCIA
    # -----------------------------------------

    if zone["type"] == "RESISTANCE":

        breakout_price = (
            zone_upper *
            (1 + BREAKOUT_MARGIN)
        )

        if (
            close > breakout_price
            and volume_confirmed
        ):
            return "BREAKOUT_UP"

    # -----------------------------------------
    # ROMPIMENTO DE SUPORTE
    # -----------------------------------------

    if zone["type"] == "SUPPORT":

        breakout_price = (
            zone_lower *
            (1 - BREAKOUT_MARGIN)
        )

        if (
            close < breakout_price
            and volume_confirmed
        ):
            return "BREAKOUT_DOWN"

    return "NO_BREAKOUT"