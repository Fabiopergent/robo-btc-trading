def classify_pivot(previous_price, current_price, pivot_type):
    """
    Classifica um pivô em relação ao pivô anterior.

    Retorna:

        HH = Higher High
        LH = Lower High
        HL = Higher Low
        LL = Lower Low
    """

    if previous_price is None:
        return None

    if pivot_type == "PIVOT_HIGH":

        if current_price > previous_price:
            return "HH"

        if current_price < previous_price:
            return "LH"

    if pivot_type == "PIVOT_LOW":

        if current_price > previous_price:
            return "HL"

        if current_price < previous_price:
            return "LL"

    return None


def detect_structure(sequence):
    """
    Analisa uma sequência de estruturas
    e determina a estrutura predominante.

    Retorna:

        UPTREND
        DOWNTREND
        SIDEWAYS
    """

    if len(sequence) < 4:
        return "SIDEWAYS"

    recent = sequence[-4:]

    # -----------------------------------------
    # TENDÊNCIA DE ALTA
    # -----------------------------------------

    bullish = (
        "HH" in recent
        and
        "HL" in recent
        and
        recent.count("HH") >= 2
        and
        recent.count("HL") >= 2
    )

    if bullish:
        return "UPTREND"

    # -----------------------------------------
    # TENDÊNCIA DE BAIXA
    # -----------------------------------------

    bearish = (
        "LH" in recent
        and
        "LL" in recent
        and
        recent.count("LH") >= 2
        and
        recent.count("LL") >= 2
    )

    if bearish:
        return "DOWNTREND"

    # -----------------------------------------
    # SEM ESTRUTURA CLARA
    # -----------------------------------------

    return "SIDEWAYS"

def build_structure(df):
    """
    Constrói a sequência de estrutura do mercado
    utilizando pivôs de 3 candles confirmados.

    Retorna uma lista contendo:

        HH
        HL
        LH
        LL
    """

    from strategy.pivots import confirm_pivot_3_candles

    structure = []

    last_high = None
    last_low = None

    for index in range(len(df)):

        pivot = confirm_pivot_3_candles(
            df,
            index
        )

        # -----------------------------------------
        # PIVOT HIGH
        # -----------------------------------------

        if pivot == "PIVOT_HIGH":

            current_high = df.iloc[index]["high"]

            classification = classify_pivot(
                last_high,
                current_high,
                "PIVOT_HIGH"
            )

            if classification:

                structure.append({
                    "index": index,
                    "type": classification,
                    "price": current_high
                })

            last_high = current_high

        # -----------------------------------------
        # PIVOT LOW
        # -----------------------------------------

        elif pivot == "PIVOT_LOW":

            current_low = df.iloc[index]["low"]

            classification = classify_pivot(
                last_low,
                current_low,
                "PIVOT_LOW"
            )

            if classification:

                structure.append({
                    "index": index,
                    "type": classification,
                    "price": current_low
                })

            last_low = current_low

    return structure