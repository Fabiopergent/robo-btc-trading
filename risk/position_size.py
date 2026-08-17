from config import RISK_PER_TRADE


def calculate_position_size(
    capital,
    entry_price,
    stop_price
):
    """
    Calcula a quantidade máxima do ativo
    que pode ser negociada respeitando
    o risco máximo por operação.

    Retorna:
        quantidade do ativo
    """

    # -----------------------------------------
    # VALOR MÁXIMO QUE PODE SER PERDIDO
    # -----------------------------------------

    risk_amount = (
        capital *
        RISK_PER_TRADE
    )

    # -----------------------------------------
    # DISTÂNCIA ATÉ O STOP
    # -----------------------------------------

    stop_distance = abs(
        entry_price - stop_price
    )

    # Evita divisão por zero
    if stop_distance == 0:
        return 0

    # -----------------------------------------
    # TAMANHO DA POSIÇÃO
    # -----------------------------------------

    quantity = (
        risk_amount /
        stop_distance
    )

    return quantity