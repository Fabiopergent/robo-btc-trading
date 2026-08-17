from config import MIN_RR


def calculate_take_profit(
    entry_price,
    stop_price,
    direction
):
    """
    Calcula o Take Profit com base
    no risco da operação.

    Utiliza o R:R mínimo definido
    no config.py.

    COMPRA:
        alvo acima da entrada.

    VENDA:
        alvo abaixo da entrada.

    Retorna:
        preço do Take Profit
    """

    # -----------------------------------------
    # DISTÂNCIA DO RISCO
    # -----------------------------------------

    risk_distance = abs(
        entry_price - stop_price
    )

    # Evita cálculo inválido
    if risk_distance == 0:
        return None

    # -----------------------------------------
    # RETORNO NECESSÁRIO
    # -----------------------------------------

    reward_distance = (
        risk_distance *
        MIN_RR
    )

    # -----------------------------------------
    # COMPRA
    # -----------------------------------------

    if direction == "BUY":

        take_profit = (
            entry_price +
            reward_distance
        )

        return take_profit

    # -----------------------------------------
    # VENDA
    # -----------------------------------------

    if direction == "SELL":

        take_profit = (
            entry_price -
            reward_distance
        )

        return take_profit

    return None