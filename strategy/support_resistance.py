import pandas as pd

from config import ZONE_TOLERANCE


def calculate_zone_range(price):
    """
    Calcula os limites de uma região de preço
    utilizando a tolerância definida no config.py.
    """

    tolerance = price * ZONE_TOLERANCE

    lower = price - tolerance
    upper = price + tolerance

    return lower, upper


def create_zones(df):
    """
    Cria regiões de suporte e resistência
    a partir dos pivôs identificados.
    """

    zones = []

    # -----------------------------------------
    # PIVOT HIGH = POSSÍVEL RESISTÊNCIA
    # -----------------------------------------

    for index, row in df[df["pivot_high"]].iterrows():

        price = row["high"]

        lower, upper = calculate_zone_range(price)

        zones.append({
            "type": "RESISTANCE",
            "price": price,
            "lower": lower,
            "upper": upper,
            "index": index
        })

    # -----------------------------------------
    # PIVOT LOW = POSSÍVEL SUPORTE
    # -----------------------------------------

    for index, row in df[df["pivot_low"]].iterrows():

        price = row["low"]

        lower, upper = calculate_zone_range(price)

        zones.append({
            "type": "SUPPORT",
            "price": price,
            "lower": lower,
            "upper": upper,
            "index": index
        })

    return zones