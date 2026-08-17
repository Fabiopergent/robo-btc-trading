import pandas as pd


def classify_pivots(df):
    """
    Classifica os pivôs encontrados como:

    HH = Higher High
    LH = Lower High
    HL = Higher Low
    LL = Lower Low
    """

    result = df.copy()

    result["pivot_type"] = None

    last_high = None
    last_low = None

    for index, row in result.iterrows():

        # -----------------------------
        # PIVOT HIGH
        # -----------------------------

        if row["pivot_high"]:

            current_high = row["high"]

            if last_high is not None:

                if current_high > last_high:
                    result.loc[index, "pivot_type"] = "HH"

                elif current_high < last_high:
                    result.loc[index, "pivot_type"] = "LH"

            last_high = current_high

        # -----------------------------
        # PIVOT LOW
        # -----------------------------

        if row["pivot_low"]:

            current_low = row["low"]

            if last_low is not None:

                if current_low > last_low:
                    result.loc[index, "pivot_type"] = "HL"

                elif current_low < last_low:
                    result.loc[index, "pivot_type"] = "LL"

            last_low = current_low

    return result


def detect_trend(df):
    """
    Identifica a tendência atual com base
    na estrutura dos pivôs.
    """

    pivot_types = df["pivot_type"].dropna().tolist()

    if len(pivot_types) < 2:
        return "UNKNOWN"

    # Últimos pivôs identificados
    recent = pivot_types[-4:]

    # Tendência de alta:
    # presença de HH e HL
    if "HH" in recent and "HL" in recent:

        # Verificação adicional para evitar
        # classificar qualquer sequência como alta.
        if recent.count("HH") >= 1 and recent.count("HL") >= 1:
            return "UPTREND"

    # Tendência de baixa:
    # presença de LH e LL
    if "LH" in recent and "LL" in recent:

        if recent.count("LH") >= 1 and recent.count("LL") >= 1:
            return "DOWNTREND"

    return "SIDEWAYS"