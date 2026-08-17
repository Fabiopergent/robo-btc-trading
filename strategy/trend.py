def detect_trend(structure):
    """
    Identifica a tendência atual com base
    na sequência dos pivôs estruturais.

    Retorna:

        UPTREND
        DOWNTREND
        SIDEWAYS
        UNKNOWN
    """

    # -----------------------------------------
    # VERIFICAR SE EXISTE ESTRUTURA
    # -----------------------------------------

    if not structure:
        return "UNKNOWN"

    # -----------------------------------------
    # PEGAR SOMENTE OS TIPOS
    # -----------------------------------------

    pivot_types = [
        item["type"]
        for item in structure
    ]

    # -----------------------------------------
    # ESTRUTURA INSUFICIENTE
    # -----------------------------------------

    if len(pivot_types) < 4:
        return "UNKNOWN"


    recent = pivot_types[-4:]

    # -----------------------------------------
    # TENDÊNCIA DE ALTA
    # -----------------------------------------

    bullish = (
        recent[0] == "HH"
        and
        recent[1] == "HL"
        and
        recent[2] == "HH"
        and
        recent[3] == "HL"
    )

    if bullish:
        return "UPTREND"

    # -----------------------------------------
    # TENDÊNCIA DE BAIXA
    # -----------------------------------------

    bearish = (
        recent[0] == "LL"
        and
        recent[1] == "LH"
        and
        recent[2] == "LL"
        and
        recent[3] == "LH"
    )

    if bearish:
        return "DOWNTREND"

    # -----------------------------------------
    # SEM CONFIRMAÇÃO
    # -----------------------------------------

    return "SIDEWAYS"