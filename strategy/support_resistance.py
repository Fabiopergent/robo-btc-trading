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

def merge_zones(zones):
    """
    Agrupa zonas do mesmo tipo que possuem
    regiões sobrepostas ou muito próximas.
    """

    if not zones:
        return []

    merged = []

    # Ordenar por preço
    sorted_zones = sorted(
        zones,
        key=lambda zone: zone["price"]
    )

    for zone in sorted_zones:

        # Primeira zona
        if not merged:

            merged.append(zone.copy())

            continue

        last = merged[-1]

        # -----------------------------------------
        # TIPOS DIFERENTES
        # -----------------------------------------

        if zone["type"] != last["type"]:

            merged.append(zone.copy())

            continue

        # -----------------------------------------
        # VERIFICAR SOBREPOSIÇÃO
        # -----------------------------------------

        overlaps = (
            zone["lower"] <= last["upper"]
            and
            zone["upper"] >= last["lower"]
        )

        if overlaps:

            last["lower"] = min(
                last["lower"],
                zone["lower"]
            )

            last["upper"] = max(
                last["upper"],
                zone["upper"]
            )

            last["price"] = (
                last["lower"] + last["upper"]
            ) / 2

        else:

            merged.append(zone.copy())

    return merged