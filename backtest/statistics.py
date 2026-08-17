def total_trades(trades):
    """
    Retorna o número total de operações.
    """

    return len(trades)


def winning_trades(trades):
    """
    Retorna a quantidade de operações vencedoras.
    """

    return sum(
        1
        for trade in trades
        if trade["profit"] > 0
    )


def losing_trades(trades):
    """
    Retorna a quantidade de operações perdedoras.
    """

    return sum(
        1
        for trade in trades
        if trade["profit"] < 0
    )


def total_profit(trades):
    """
    Calcula o lucro ou prejuízo total.
    """

    return sum(
        trade["profit"]
        for trade in trades
    )


def win_rate(trades):
    """
    Calcula a porcentagem de operações vencedoras.
    """

    if not trades:
        return 0

    wins = winning_trades(trades)

    return (
        wins /
        len(trades)
    ) * 100

def profit_factor(trades):
    """
    Calcula o Profit Factor.

    Fórmula:

        lucro bruto / perda bruta
    """

    gross_profit = sum(
        trade["profit"]
        for trade in trades
        if trade["profit"] > 0
    )

    gross_loss = sum(
        abs(trade["profit"])
        for trade in trades
        if trade["profit"] < 0
    )

    if gross_loss == 0:
        return None

    return gross_profit / gross_loss


def largest_win(trades):
    """
    Retorna o maior lucro individual.
    """

    profits = [
        trade["profit"]
        for trade in trades
        if trade["profit"] > 0
    ]

    if not profits:
        return 0

    return max(profits)


def largest_loss(trades):
    """
    Retorna a maior perda individual.
    """

    losses = [
        trade["profit"]
        for trade in trades
        if trade["profit"] < 0
    ]

    if not losses:
        return 0

    return min(losses)


def average_profit(trades):
    """
    Calcula o resultado médio por operação.
    """

    if not trades:
        return 0

    return (
        total_profit(trades) /
        len(trades)
    )