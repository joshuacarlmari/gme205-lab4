from shapely.geometry import shape

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = shape(geometry)

    def area(self):
        return self._area_sqm


class Parcel(SpatialObject):
    def __init__(self, parcel_id, zone, is_active, area_sqm, geometry):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.zone = zone
        self.is_active = is_active
        self._area_sqm = area_sqm 

    def is_in_zone(self, zone_name):
        return self.zone == zone_name