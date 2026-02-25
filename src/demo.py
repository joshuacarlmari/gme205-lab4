import json
from spatial import Parcel
import analysis


def load_parcels(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)

    parcels = []

    for item in data:  # Repetition
        parcel = Parcel(
            parcel_id=item["parcel_id"],
            zone=item["zone"],
            is_active=item["is_active"],
            area_sqm=item["area_sqm"],
            geometry=item["geometry"]
        )
        parcels.append(parcel)

    return parcels


def main():

    # 1️⃣ Sequence — Load data
    parcels = load_parcels("data/parcels.json")

    # 2️⃣ Selection
    if not parcels:
        print("Error: No parcels found.")
        return

    # 3️⃣ Repetition inside analysis functions
    total_area = analysis.total_active_area(parcels)
    large_parcels = analysis.parcels_above_threshold(parcels, 5000)
    zone_counts = analysis.count_by_zone(parcels)
    residential_parcels = analysis.intersecting_parcels(parcels, "Residential")

    # Print results
    print("Total Active Area:", total_area)
    print("Parcels Above Threshold:", [p.parcel_id for p in large_parcels])
    print("Parcels per Zone:", zone_counts)
    print("Residential Parcels:", [p.parcel_id for p in residential_parcels])

    # Save summary
    summary = {
        "total_active_area": total_area,
        "parcels_above_threshold": [p.parcel_id for p in large_parcels],
        "zone_counts": zone_counts,
        "residential_parcels": [p.parcel_id for p in residential_parcels]
    }

    with open("output/summary.json", "w") as f:
        json.dump(summary, f, indent=4)


if __name__ == "__main__":
    main()