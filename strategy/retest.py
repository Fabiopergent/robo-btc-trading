import pandas as pd

from config import MAX_RETEST_CANDLES


def candle_touches_zone(candle, zone):
    """
    Verifica se o candle tocou ou entrou
    na região de suporte/resistência.
    """

    candle_high = candle["high"]
    candle_low = candle["low"]

    zone_lower = zone["lower"]
    zone_upper = zone["upper"]

    # Existe sobreposição entre o candle e a zona?
    return (
        candle_high >= zone_lower
        and candle_low <= zone_upper
    )


def bullish_rejection(candle, zone):
    """
    Verifica uma rejeição para cima.

    O candle deve tocar a região e fechar acima dela.
    """

    if not candle_touches_zone(candle, zone):
        return False

    return candle["close"] > zone["upper"]


def bearish_rejection(candle, zone):
    """
    Verifica uma rejeição para baixo.

    O candle deve tocar a região e fechar abaixo dela.
    """

    if not candle_touches_zone(candle, zone):
        return False

    return candle["close"] < zone["lower"]


def check_retest(df, breakout_index, zone, breakout_direction):
    """
    Procura um reteste depois de um rompimento confirmado.

    Retorna:

        RETEST_UP
        RETEST_DOWN
        NO_RETEST
    """

    start = breakout_index + 1

    end = min(
        breakout_index + 1 + MAX_RETEST_CANDLES,
        len(df)
    )

    for index in range(start, end):

        candle = df.iloc[index]

        # -----------------------------------------
        # RETESTE APÓS ROMPIMENTO PARA CIMA
        # -----------------------------------------

        if breakout_direction == "BREAKOUT_UP":

            if bullish_rejection(candle, zone):

                return {
                    "result": "RETEST_UP",
                    "index": index
                }

        # -----------------------------------------
        # RETESTE APÓS ROMPIMENTO PARA BAIXO
        # -----------------------------------------

        elif breakout_direction == "BREAKOUT_DOWN":

            if bearish_rejection(candle, zone):

                return {
                    "result": "RETEST_DOWN",
                    "index": index
                }

    return {
        "result": "NO_RETEST",
        "index": None
    }