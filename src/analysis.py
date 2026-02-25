def total_active_area(parcels: list) -> float:
    total = 0.0

    for parcel in parcels:  # Repetition
        if parcel.is_active:  # Selection
            total += parcel.area()

    return total


def parcels_above_threshold(parcels: list, threshold: float) -> list:
    result = []

    for parcel in parcels:
        if parcel.area() > threshold:
            result.append(parcel)

    return result


def count_by_zone(parcels: list) -> dict:
    counts = {}

    for parcel in parcels:
        zone = parcel.zone

        if zone not in counts:
            counts[zone] = 0

        counts[zone] += 1

    return counts


def intersecting_parcels(parcels: list, zone: str) -> list:
    """
    For this lab:
    'Intersection' is defined as parcels suitable
    for development by zone.
    """

    selected = []

    for parcel in parcels:
        if parcel.is_in_zone(zone):
            selected.append(parcel)

    return selected