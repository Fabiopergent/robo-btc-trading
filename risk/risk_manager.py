from risk.position_size import calculate_position_size
from risk.stop_loss import calculate_stop_loss
from risk.take_profit import calculate_take_profit


def calculate_trade_risk(
    capital,
    entry_price,
    zone,
    direction
):
    """
    Integra os componentes de gerenciamento
    de risco de uma operação.

    Calcula:

        Stop Loss
        Take Profit
        Position Size
        Risco financeiro
        Relação R:R
    """

    # -----------------------------------------
    # STOP LOSS
    # -----------------------------------------

    stop_price = calculate_stop_loss(
        entry_price,
        zone,
        direction
    )

    if stop_price is None:
        return None

    # -----------------------------------------
    # TAKE PROFIT
    # -----------------------------------------

    take_profit = calculate_take_profit(
        entry_price,
        stop_price,
        direction
    )

    if take_profit is None:
        return None

    # -----------------------------------------
    # POSITION SIZE
    # -----------------------------------------

    quantity = calculate_position_size(
        capital,
        entry_price,
        stop_price
    )

    if quantity <= 0:
        return None

    # -----------------------------------------
    # RISCO FINANCEIRO
    # -----------------------------------------

    risk_per_unit = abs(
        entry_price - stop_price
    )

    risk_amount = (
        risk_per_unit *
        quantity
    )

    # -----------------------------------------
    # RETORNO FINANCEIRO
    # -----------------------------------------

    reward_per_unit = abs(
        take_profit - entry_price
    )

    reward_amount = (
        reward_per_unit *
        quantity
    )

    # -----------------------------------------
    # R:R REAL
    # -----------------------------------------

    if risk_amount == 0:
        return None

    risk_reward = (
        reward_amount /
        risk_amount
    )

    # -----------------------------------------
    # RESULTADO
    # -----------------------------------------

    return {
        "direction": direction,
        "entry": entry_price,
        "stop": stop_price,
        "target": take_profit,
        "quantity": quantity,
        "risk_amount": risk_amount,
        "reward_amount": reward_amount,
        "risk_reward": risk_reward
    }