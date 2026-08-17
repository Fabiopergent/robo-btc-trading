def evaluate_setup(
    trend,
    breakout,
    retest,
    price_action,
    volume_confirmed
):
    """
    Avalia se existe um setup completo
    de compra ou venda.

    Retorna:
        BUY
        SELL
        NO_TRADE
    """

    # -----------------------------------------
    # COMPRA
    # -----------------------------------------

    if trend == "UPTREND":

        if breakout == "BREAKOUT_UP":

            if retest == "RETEST_UP":

                bullish_patterns = [
                    "HAMMER",
                    "BULLISH_ENGULFING",
                    "INVERTED_HAMMER"
                ]

                if price_action in bullish_patterns:

                    if volume_confirmed:
                        return "BUY"

    # -----------------------------------------
    # VENDA
    # -----------------------------------------

    if trend == "DOWNTREND":

        if breakout == "BREAKOUT_DOWN":

            if retest == "RETEST_DOWN":

                bearish_patterns = [
                    "BEARISH_ENGULFING"
                ]

                if price_action in bearish_patterns:
                    if volume_confirmed:
                        return "SELL"

    # -----------------------------------------
    # NENHUM SETUP
    # -----------------------------------------

    return "NO_TRADE"