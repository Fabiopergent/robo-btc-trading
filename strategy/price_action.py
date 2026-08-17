def candle_anatomy(candle):
    """
    Calcula a anatomia básica de um candle.
    """

    open_price = candle["open"]
    close_price = candle["close"]
    high = candle["high"]
    low = candle["low"]

    body = abs(close_price - open_price)

    upper_wick = high - max(open_price, close_price)

    lower_wick = min(open_price, close_price) - low

    total_range = high - low

    return {
        "body": body,
        "upper_wick": upper_wick,
        "lower_wick": lower_wick,
        "range": total_range
    }


def is_bullish(candle):
    """
    Verifica se o candle é de alta.
    """

    return candle["close"] > candle["open"]


def is_bearish(candle):
    """
    Verifica se o candle é de baixa.
    """

    return candle["close"] < candle["open"]


def is_hammer(candle):
    """
    Identifica um possível martelo.

    Regras:
    - pavio inferior >= 2x o corpo
    - pavio superior <= 0.5x o corpo
    """

    anatomy = candle_anatomy(candle)

    body = anatomy["body"]
    upper_wick = anatomy["upper_wick"]
    lower_wick = anatomy["lower_wick"]

    if body == 0:
        return False

    return (
        lower_wick >= body * 2
        and upper_wick <= body
    )


def is_inverted_hammer(candle):
    """
    Identifica um possível martelo invertido.

    Regras:
    - pavio superior >= 2x o corpo
    - pavio inferior <= 0.5x o corpo
    """

    anatomy = candle_anatomy(candle)

    body = anatomy["body"]
    upper_wick = anatomy["upper_wick"]
    lower_wick = anatomy["lower_wick"]

    if body == 0:
        return False

    return (
        upper_wick >= body * 2
        and lower_wick <= body
    )


def is_doji(candle):
    """
    Identifica um Doji.

    O corpo representa no máximo 10%
    do range total.

    Martelos não são classificados como Doji.
    """

    anatomy = candle_anatomy(candle)

    body = anatomy["body"]
    total_range = anatomy["range"]

    if total_range == 0:
        return False

    if is_hammer(candle):
        return False

    if is_inverted_hammer(candle):
        return False

    return body <= total_range * 0.10


def is_bullish_engulfing(previous, current):
    """
    Identifica um engolfo de alta.
    """

    previous_bearish = (
        previous["close"] < previous["open"]
    )

    current_bullish = (
        current["close"] > current["open"]
    )

    previous_body_low = min(
        previous["open"],
        previous["close"]
    )

    previous_body_high = max(
        previous["open"],
        previous["close"]
    )

    current_body_low = min(
        current["open"],
        current["close"]
    )

    current_body_high = max(
        current["open"],
        current["close"]
    )

    body_engulfs = (
        current_body_low <= previous_body_low
        and current_body_high >= previous_body_high
    )

    return (
        previous_bearish
        and current_bullish
        and body_engulfs
    )


def is_bearish_engulfing(previous, current):
    """
    Identifica um engolfo de baixa.
    """

    previous_bullish = (
        previous["close"] > previous["open"]
    )

    current_bearish = (
        current["close"] < current["open"]
    )

    previous_body_low = min(
        previous["open"],
        previous["close"]
    )

    previous_body_high = max(
        previous["open"],
        previous["close"]
    )

    current_body_low = min(
        current["open"],
        current["close"]
    )

    current_body_high = max(
        current["open"],
        current["close"]
    )

    body_engulfs = (
        current_body_low <= previous_body_low
        and current_body_high >= previous_body_high
    )

    return (
        previous_bullish
        and current_bearish
        and body_engulfs
    )


def detect_candle_pattern(previous, current):
    """
    Detecta o padrão de Price Action mais relevante.
    """

    if is_bullish_engulfing(previous, current):
        return "BULLISH_ENGULFING"

    if is_bearish_engulfing(previous, current):
        return "BEARISH_ENGULFING"

    if is_hammer(current):
        return "HAMMER"

    if is_inverted_hammer(current):
        return "INVERTED_HAMMER"

    if is_doji(current):
        return "DOJI"

    return "NONE"