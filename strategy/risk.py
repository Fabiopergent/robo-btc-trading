def calculate_risk_amount(
    balance,
    risk_percent=0.01
):
    """
    Calcula quanto da conta pode ser perdido
    na operação.

    Exemplo:

    R$100 × 1% = R$1
    """

    return balance * risk_percent


def calculate_position_size(
    entry_price,
    stop_price,
    risk_amount
):
    """
    Calcula a quantidade do ativo que pode ser
    comprada/vendida para respeitar o risco
    financeiro definido.
    """

    stop_distance = abs(
        entry_price - stop_price
    )

    if stop_distance <= 0:
        return 0

    position_size = (
        risk_amount /
        stop_distance
    )

    return position_size


def calculate_target(
    entry_price,
    stop_price,
    risk_reward=3
):
    """
    Calcula o alvo usando o R:R definido.

    R:R 1:3 significa que o alvo fica a
    três vezes a distância do stop.
    """

    risk_distance = abs(
        entry_price - stop_price
    )

    # Entrada acima do stop = operação de compra
    if entry_price > stop_price:

        target = (
            entry_price +
            risk_distance * risk_reward
        )

    # Entrada abaixo do stop = operação de venda
    else:

        target = (
            entry_price -
            risk_distance * risk_reward
        )

    return target