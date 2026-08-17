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

    Exemplo:

    volume atual = 2000
    média = 1000

    resultado = 2.0
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
    multiplier=1.5,
    lookback=20
):
    """
    Verifica se o volume atual é pelo menos
    1.5x a média dos candles anteriores.
    """

    ratio = volume_ratio(
        df,
        index,
        lookback
    )

    if ratio is None:
        return False

    return ratio >= multiplier