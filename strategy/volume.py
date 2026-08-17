from config import (
    BREAKOUT_VOLUME_MULTIPLIER,
    CONFIRMATION_VOLUME_MULTIPLIER
)


def average_volume(df, index, lookback=20):
    """
    Calcula o volume médio dos candles anteriores
    ao candle atual.
    """

    if index < lookback:
        return None

    previous_volumes = df.iloc[
        index - lookback:index
    ]["volume"]

    return previous_volumes.mean()


def volume_ratio(df, index, lookback=20):
    """
    Calcula quantas vezes o volume atual é maior
    ou menor que a média anterior.
    """

    avg = average_volume(
        df,
        index,
        lookback
    )

    if avg is None or avg == 0:
        return None

    current_volume = df.iloc[index]["volume"]

    return current_volume / avg


def is_volume_confirmed(
    df,
    index,
    multiplier=BREAKOUT_VOLUME_MULTIPLIER,
    lookback=20
):
    """
    Verifica se o volume atual é suficiente
    para confirmar um rompimento.
    """

    ratio = volume_ratio(
        df,
        index,
        lookback
    )

    if ratio is None:
        return False

    return ratio >= multiplier


def is_confirmation_volume(
    df,
    index,
    lookback=20
):
    """
    Verifica se o volume atual é suficiente
    para confirmar a retomada após um reteste.
    """

    ratio = volume_ratio(
        df,
        index,
        lookback
    )

    if ratio is None:
        return False

    return ratio >= CONFIRMATION_VOLUME_MULTIPLIER