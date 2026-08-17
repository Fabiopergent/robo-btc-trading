def calculate_stop_loss(
    entry_price,
    zone,
    direction
):
    """
    Calcula o Stop Loss com base na região
    de suporte ou resistência.

    COMPRA:
        Stop abaixo da região.

    VENDA:
        Stop acima da região.

    Retorna:
        preço do Stop Loss
    """

    zone_lower = zone["lower"]
    zone_upper = zone["upper"]

    # -----------------------------------------
    # COMPRA
    # -----------------------------------------

    if direction == "BUY":

        stop_price = zone_lower

        return stop_price

    # -----------------------------------------
    # VENDA
    # -----------------------------------------

    if direction == "SELL":

        stop_price = zone_upper

        return stop_price

    return None